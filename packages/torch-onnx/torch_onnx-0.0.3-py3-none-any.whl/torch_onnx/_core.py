from __future__ import annotations

import ctypes
import inspect
import itertools
import logging
import operator
import typing
from typing import Any, Sequence

import numpy as np
import torch
import torch.fx
from onnxscript import ir
from onnxscript.ir import _convenience as ir_convenience
from torch.export import graph_signature

logger = logging.getLogger(__name__)
# Define utilities to convert PyTorch data types so users do not need to specify manually
_TORCH_DTYPE_TO_ONNX: dict[torch.dtype, ir.DataType] = {
    torch.bfloat16: ir.DataType.BFLOAT16,
    torch.bool: ir.DataType.BOOL,
    torch.complex128: ir.DataType.COMPLEX128,
    torch.complex64: ir.DataType.COMPLEX64,
    torch.float16: ir.DataType.FLOAT16,
    torch.float32: ir.DataType.FLOAT,
    torch.float64: ir.DataType.DOUBLE,
    torch.float8_e4m3fn: ir.DataType.FLOAT8E4M3FN,
    torch.float8_e4m3fnuz: ir.DataType.FLOAT8E4M3FNUZ,
    torch.float8_e5m2: ir.DataType.FLOAT8E5M2,
    torch.float8_e5m2fnuz: ir.DataType.FLOAT8E5M2FNUZ,
    torch.int16: ir.DataType.INT16,
    torch.int32: ir.DataType.INT32,
    torch.int64: ir.DataType.INT64,
    torch.int8: ir.DataType.INT8,
    torch.uint8: ir.DataType.UINT8,
}


def _torch_dtype_to_onnx_dtype(dtype: torch.dtype) -> ir.DataType:
    return _TORCH_DTYPE_TO_ONNX[dtype]


class TorchTensor(ir.Tensor):
    def __init__(self, tensor: torch.Tensor, name: str | None = None):
        # Pass the tensor as the raw data to ir.Tensor's constructor
        super().__init__(
            tensor, dtype=_torch_dtype_to_onnx_dtype(tensor.dtype), name=name
        )

    def __array__(self, dtype: Any = None) -> np.ndarray:
        # numpy() calls __array__ in ir.Tensor
        if self.dtype == ir.DataType.BFLOAT16:
            return self.raw.view(torch.uint16).__array__(dtype)
        if self.dtype in {
            ir.DataType.FLOAT8E4M3FN,
            ir.DataType.FLOAT8E4M3FNUZ,
            ir.DataType.FLOAT8E5M2,
            ir.DataType.FLOAT8E5M2FNUZ,
        }:
            # TODO: Use ml_dtypes
            return self.raw.view(torch.uint8).__array__(dtype)
        return self.raw.__array__(dtype)

    def tobytes(self) -> bytes:
        # Implement tobytes to support native PyTorch types so we can use types like bloat16
        # Reading from memory directly is also more efficient because
        # it avoids copying to a NumPy array
        tensor = self.raw.detach().cpu().contiguous()
        return bytes(
            (ctypes.c_ubyte * tensor.element_size() * tensor.numel()).from_address(
                tensor.data_ptr()
            )
        )


# https://github.com/pytorch/pytorch/blob/ee6cb6daa173896f8ea1876266a19775aaa4f610/torch/export/graph_signature.py#L56C1-L62C19
# class InputKind(Enum):
#     USER_INPUT = auto()
#     PARAMETER = auto()
#     BUFFER = auto()
#     CONSTANT_TENSOR = auto()
#     CUSTOM_OBJ = auto()
#     TOKEN = auto()

# https://github.com/pytorch/pytorch/blob/ee6cb6daa173896f8ea1876266a19775aaa4f610/torch/export/graph_signature.py#L89C1-L96C19
# class OutputKind(Enum):
#     USER_OUTPUT = auto()
#     LOSS_OUTPUT = auto()
#     BUFFER_MUTATION = auto()
#     GRADIENT_TO_PARAMETER = auto()
#     GRADIENT_TO_USER_INPUT = auto()
#     USER_INPUT_MUTATION = auto()
#     TOKEN = auto()


def _set_shape_types(values: Sequence[ir.Value], meta_vals: Sequence[torch.Tensor]):
    for value, meta_val in zip(values, meta_vals):
        _set_shape_type(value, meta_val)


def _set_shape_type(value: ir.Value, meta_val: torch.Tensor | tuple[torch.Tensor]):
    if isinstance(meta_val, tuple):
        logger.warning("Setting shape and type of tensors is not supported yet")
    if isinstance(meta_val, torch.Tensor):
        dims = []
        for dim in meta_val.shape:
            if isinstance(dim, int):
                dims.append(dim)
            else:
                dims.append(str(dim.node))
        value.dtype = _torch_dtype_to_onnx_dtype(meta_val.dtype)
        value.shape = ir.Shape(dims)
    elif isinstance(meta_val, (int, torch.SymInt)):
        # aten::sym_size output is a int, not a tensor, which stands
        # for the size of one dim. We treat it as a scalar.
        value.dtype = ir.DataType.INT64
        value.shape = ir.Shape([])
    elif isinstance(meta_val, (bool, torch.SymBool)):
        value.dtype = ir.DataType.BOOL
        value.shape = ir.Shape([])
    elif isinstance(meta_val, (float, torch.SymFloat)):
        value.dtype = ir.DataType.FLOAT
        value.shape = ir.Shape([])
    else:
        pass


def _get_qualified_module_name(cls: Any) -> str:
    module = cls.__module__
    if module is None or module == str.__class__.__module__:
        return cls.__name__
    return module + "." + cls.__name__


def _get_node_namespace(node: torch.fx.Node) -> tuple[str, list[str], list[str]]:
    """Get the namespace and scope of the node.

    Example::

        {
            'L__self__': ('', <class 'torchvision.models.resnet.ResNet'>),
            'L__self___avgpool': ('avgpool', <class 'torch.nn.modules.pooling.AdaptiveAvgPool2d'>)
        }

    Will yield

    namespace: ": torchvision.models.resnet.ResNet/avgpool: torch.nn.modules.pooling.AdaptiveAvgPool2d"
    class_hierarchy: ["torchvision.models.resnet.ResNet", "torch.nn.modules.pooling.AdaptiveAvgPool2d"]
    name_scopes: ["", "avgpool"]

    Args:
        node: The node to get the namespace and scope of.

    Returns:
        (namespace, class_hierarchy, name_scope)
    """
    nn_module_stack = node.meta.get("nn_module_stack")
    logger.debug("%s", nn_module_stack)
    if nn_module_stack is None:
        logging.warning("nn_module_stack not found for node %s", node.name)
        return "", [], []
    namespaces = []
    class_hierarchy = []
    name_scopes = []
    for name, nn_module in nn_module_stack.values():
        name_scopes.append(name)
        nn_module_name = _get_qualified_module_name(nn_module)
        class_hierarchy.append(nn_module_name)
        namespaces.append(f"{name}: {_get_qualified_module_name(nn_module)}")

    return "/".join(namespaces), class_hierarchy, name_scopes


def _set_namespace(node: torch.fx.Node, ir_node: ir.Node):
    nn_module_stack = node.meta.get("nn_module_stack")
    node.meta["nn_module_stack"] = nn_module_stack
    namespace, class_hierarchy, name_scopes = _get_node_namespace(node)
    ir_node.metadata_props["namespace"] = namespace
    ir_node.metadata_props["class_hierarchy"] = repr(class_hierarchy)
    ir_node.metadata_props["name_scopes"] = repr(name_scopes)


def _handle_getitem_node(
    node: torch.fx.Node, node_name_to_values: dict[str, ir.Value | Sequence[ir.Value]]
) -> ir.Value:
    """Handle a getitem node.

    Add the input value it is getting to the mapping, then return the value.
    """
    assert len(node.all_input_nodes) == 1
    source = node.all_input_nodes[0]
    source_outputs = node_name_to_values[source.name]
    assert isinstance(
        source_outputs, Sequence
    ), f"Expected {source.name} to output sequence, got {node_name_to_values[source.name]}"
    index = typing.cast(int, node.args[1])
    value = source_outputs[index]
    # Save the getitem value to the values mapping to in case
    # it is one of the graph outputs
    node_name_to_values[node.name] = value
    return value


def _add_nodes(
    exported_program: torch.export.ExportedProgram, graph: ir.Graph
) -> dict[str, ir.Value]:
    node_name_to_values: dict[str, ir.Value | Sequence[ir.Value]] = {}
    for node in exported_program.graph.nodes:
        logger.debug(
            "%s", (node.name, node.args, node.target, node.op, node.type, node.kwargs)
        )
        if node.op == "placeholder":
            # Placeholder nodes are user inputs
            # We need to create a new tensor for each user input
            # and add it to the graph's inputs
            name = node.name
            # shape = node.kwargs["shape"]
            # dtype = node.kwargs["dtype"]
            input_ = ir.Input(name)
            input_.meta["node"] = node
            node_name_to_values[name] = input_
            # The inputs will be added to the graph later
        elif node.op == "call_function":
            if node.target == operator.getitem:
                _handle_getitem_node(node, node_name_to_values)
                continue
            # Add op to the graph
            op = str(node.target)
            fx_inputs, attributes, input_names, output_names = (
                _get_inputs_and_attributes(node)
            )
            inputs = []
            for i, input_ in enumerate(fx_inputs):
                if input_ is None:
                    inputs.append(None)
                elif hasattr(input_, "name"):
                    if (
                        isinstance(input_, torch.fx.Node)
                        and input_.target == operator.getitem
                    ):
                        actual_input = _handle_getitem_node(input_, node_name_to_values)
                        inputs.append(actual_input)
                    else:
                        inputs.append(node_name_to_values[input_.name])
                else:
                    attributes[f"arg_{i}"] = input_

            outputs = [ir.Value(name=name) for name in output_names]
            if len(outputs) > 1:
                _set_shape_types(outputs, node.meta["val"])
                node_name_to_values[node.name] = outputs
            else:
                _set_shape_type(outputs[0], node.meta["val"])
                node_name_to_values[node.name] = outputs[0]

            ir_node = ir.Node(
                "pkg.torch.ops",
                op,
                inputs,
                attributes=ir_convenience.convert_attributes(attributes),
                outputs=outputs,
                name=node.name,
            )
            ir_node.meta["node"] = node
            ir_node.metadata_props["fx_node"] = str(node.format_node())
            ir_node.metadata_props["input_names"] = repr(input_names)
            # Record the nn.Module stack for the node
            _set_namespace(node, ir_node)

            graph.append(ir_node)
    return node_name_to_values


def _torch_version_integer() -> int:
    return int(torch.__version__.replace(".", ""))


def _get_inputs_and_attributes(
    node: torch.fx.Node,
) -> tuple[list[torch.fx.Node | None], dict[str, Any], list[str], list[str]]:
    """Find and Fill in the not provided kwargs with default values.

    Returns:
        (inputs, attributes, input_names, output_names)
    """
    if inspect.isbuiltin(node.target) or isinstance(node.target, str):
        inputs = list(node.args)
        return inputs, {}, [], [node.name]

    # The target should be an ATen operator now
    node_schema = node.target._schema

    # This function assumes the order of arguments in FX op is the
    # same as the order of arguments in TorchScript op.
    inputs = []
    input_names = []
    attributes = {}

    if inspect.isbuiltin(node.target):
        inputs = list(node.args)
    else:
        for arg, schema_arg in zip(node.args, node_schema.arguments):
            if arg is None or isinstance(arg, torch.fx.Node):
                inputs.append(arg)
                input_names.append(schema_arg.name)
            else:
                attributes[schema_arg.name] = arg
        for schema_arg in node_schema.arguments:
            if schema_arg.name not in node.kwargs:
                continue
            if schema_arg.name in {
                "layout",
                "device",
                "requires_grad",
                "memory_format",
                "implicit",
            }:
                attr = str(node.kwargs[schema_arg.name])
            if schema_arg.name == "dtype":
                attr = _torch_dtype_to_onnx_dtype(node.kwargs[schema_arg.name])
            else:
                attr = node.kwargs[schema_arg.name]

            attributes[schema_arg.name] = attr

    output_names = [f"{node.name}_{output.name}" for output in node_schema.returns]

    return inputs, attributes, input_names, output_names


def exported_program_to_ir_graph(exported_program: torch.export.ExportedProgram):
    # TODO: Make it an Interpreter
    graph = ir.Graph(
        [],
        [],
        nodes=[],
        opset_imports={"": 20, "pkg.torch.ops": _torch_version_integer()},
        name="main_graph",
    )

    # TODO: We can call exported_program.graph.eliminate_dead_code()

    # 1. Add all nodes to the graph and create a dictionary of values
    values = _add_nodes(exported_program, graph)

    # 2. Add user inputs and all parameters/buffers to the graph.
    # Since the node names and the tensor names are different, we need to rename
    # the nodes to match the tensor names later. For now we will just use the node names.
    user_inputs = [
        spec
        for spec in exported_program.graph_signature.input_specs
        if spec.kind == graph_signature.InputKind.USER_INPUT
    ]
    non_user_inputs = [
        spec
        for spec in exported_program.graph_signature.input_specs
        if spec.kind != graph_signature.InputKind.USER_INPUT
    ]

    for spec in itertools.chain(user_inputs, non_user_inputs):
        # Put the user inputs first and then the parameters/buffers
        value_name = spec.arg.name
        input_kind = spec.kind
        persistent = spec.persistent
        value = values[value_name]

        value.metadata_props["pkg.torch.export.graph_signature.InputSpec.kind"] = (
            input_kind.name
        )
        value.metadata_props[
            "pkg.torch.export.graph_signature.InputSpec.persistent"
        ] = str(persistent)

        graph.inputs.append(value)  # type: ignore
        if input_kind != graph_signature.InputKind.USER_INPUT:
            graph.initializers[value_name] = value

    # 3. Add outputs to the graph. Keep the order of the outputs.
    for spec in exported_program.graph_signature.output_specs:
        value_name = spec.arg.name
        output_kind = spec.kind
        value = values[value_name]

        value.metadata_props["pkg.torch.export.graph_signature.OutputSpec.kind"] = (
            output_kind.name
        )

        if output_kind == graph_signature.OutputKind.USER_OUTPUT:
            graph.outputs.append(value)

    # 4. Rename the initializers to match the tensor names
    for name, param_name in itertools.chain(
        exported_program.graph_signature.inputs_to_parameters.items(),
        exported_program.graph_signature.inputs_to_buffers.items(),
    ):
        initializer = graph.initializers.pop(name)
        initializer.name = param_name
        graph.initializers[param_name] = initializer

    # 5. Add initializers to the graph
    for name, value in graph.initializers.items():
        torch_tensor = exported_program.state_dict.get(name)
        if torch_tensor is None:
            logger.warning("Tensor '%s' not found in state_dict", name)
            continue
        ir_tensor = TorchTensor(torch_tensor, name=name)
        graph.initializers[name].const_value = ir_tensor
        _set_shape_type(graph.initializers[name], torch_tensor)

    # TODO: Decide if we should keep mutated buffers as inputs/outputs

    return graph


def exported_program_to_ir(exported_program: torch.export.ExportedProgram) -> ir.Model:
    return ir.Model(
        exported_program_to_ir_graph(exported_program),
        ir_version=9,
        producer_name="torch",
        producer_version=torch.__version__,
    )
