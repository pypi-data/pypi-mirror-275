import functools
from typing import Any, Callable, Optional, Tuple, Union

import torch
import torch.nn as nn
from torch import Tensor
from torch.nn.parameter import Parameter

from classiq.applications.qnn.circuit_utils import (
    extract_parameters,
    is_single_layer_circuit,
    map_parameters,
    validate_circuit,
)
from classiq.applications.qnn.gradients.simple_quantum_gradient import (
    SimpleQuantumGradient,
)
from classiq.applications.qnn.torch_utils import (
    einsum_inputs,
    einsum_weigths,
    iter_inputs_weights,
)
from classiq.applications.qnn.types import (
    Circuit,
    ExecuteFunction,
    MultipleArguments,
    PostProcessFunction,
)
from classiq.exceptions import ClassiqQNNError, ClassiqTorchError
from classiq.synthesis import SerializedQuantumProgram


class QLayerFunction(torch.autograd.Function):
    @staticmethod
    def forward(  # type: ignore[override]
        ctx: Any,
        inputs: Tensor,
        weights: Tensor,
        quantum_program: SerializedQuantumProgram,
        execute: ExecuteFunction,
        post_process: PostProcessFunction,
    ) -> Tensor:
        """
        This function receives:
            inputs: a 2D Tensor of floats - (batch_size, in_features)
            weights: a 2D Tensor of floats - (out_features, num_weights)
            circuit: a `GeneratedCircuit` object
            execute: a function taking a `GeneratedCircuit` and `MultipleArguments`
                and returning `MultipleExecutionDetails`
            post_process: a function taking a single `ExecutionDetails`
                and returning a `Tensor`

        """
        circuit = Circuit.parse_raw(quantum_program)
        validate_circuit(circuit)

        # save for backward
        ctx.save_for_backward(inputs, weights)
        ctx.quantum_program = quantum_program
        ctx.execute = execute
        ctx.post_process = post_process
        ctx.quantum_gradient = SimpleQuantumGradient(
            quantum_program, execute, post_process
        )

        ctx.batch_size, ctx.num_in_features = inputs.shape
        if is_single_layer_circuit(weights):
            ctx.num_weights = weights.shape
        else:
            ctx.num_out_features, ctx.num_weights = weights.shape

        # Todo: avoid computing `_get_extracted_parameters` on every `forward`
        extracted_parameters = extract_parameters(circuit)

        # Todo: avoid defining `convert_tensors_to_arguments` on every `forward`
        def convert_tensors_to_arguments(
            inputs_: Tensor, weights_: Tensor
        ) -> MultipleArguments:
            arguments = map_parameters(
                extracted_parameters,
                inputs_,
                weights_,
            )
            return (arguments,)

        return iter_inputs_weights(
            inputs,
            weights,
            convert_tensors_to_arguments,
            functools.partial(execute, quantum_program),
            post_process,
        )

    @staticmethod
    def backward(  # type: ignore[override]
        ctx: Any, grad_output: Tensor
    ) -> Tuple[Optional[Tensor], Optional[Tensor], None, None, None]:
        """
        grad_output: Tensor
            is of shape (ctx.batch_size, ctx.num_out_features)
        """
        inputs, weights = ctx.saved_tensors

        grad_weights = grad_inputs = None
        grad_circuit = grad_execute = grad_post_process = None
        is_single_layer = is_single_layer_circuit(weights)

        if ctx.needs_input_grad[1]:
            grad_weights = ctx.quantum_gradient.gradient_weights(inputs, weights)
            grad_weights = einsum_weigths(grad_output, grad_weights, is_single_layer)

        if ctx.needs_input_grad[0]:
            grad_inputs = ctx.quantum_gradient.gradient_inputs(inputs, weights)
            grad_inputs = einsum_inputs(grad_output, grad_inputs, is_single_layer)

        if any(ctx.needs_input_grad[i] for i in (2, 3, 4)):
            raise ClassiqTorchError(
                f"Grad required for unknown type: {ctx.needs_input_grad}"
            )

        return grad_inputs, grad_weights, grad_circuit, grad_execute, grad_post_process


CalcNumOutFeatures = Callable[[SerializedQuantumProgram], int]


def calc_num_out_features_single_output(
    quantum_program: SerializedQuantumProgram,
) -> int:
    return 1


# Todo: extend the input to allow for multiple `qcode` - one for each output
#   thus allowing (something X n) instead of (something X 1) output
class QLayer(nn.Module):
    def __init__(
        self,
        quantum_program: SerializedQuantumProgram,
        execute: ExecuteFunction,
        post_process: PostProcessFunction,
        # Optional parameters:
        head_start: Union[float, Tensor, None] = None,
        # Experimental parameters:
        calc_num_out_features: CalcNumOutFeatures = calc_num_out_features_single_output,
    ) -> None:
        circuit = Circuit.parse_raw(quantum_program)
        validate_circuit(circuit)

        super().__init__()

        self._execute = execute
        self._post_process = post_process
        self._head_start = head_start

        self.quantum_program = quantum_program

        weights, _ = extract_parameters(circuit)
        self.in_features: int = len(weights)
        self.out_features: int = calc_num_out_features(quantum_program)

        self._initialize_parameters()

    def _initialize_parameters(self) -> None:
        shape: Tuple[int, ...] = (
            (self.out_features, self.in_features)
            if self.out_features > 1
            else (self.in_features,)
        )

        if self._head_start is None:
            value = torch.rand(shape)
        elif isinstance(self._head_start, (float, int)):
            value = torch.zeros(shape) + self._head_start
        elif isinstance(self._head_start, Tensor):
            value = self._head_start.clone()
        else:
            raise ClassiqQNNError(
                f"Unsupported feature - head_start of type {type(self._head_start)}"
            )

        self.weight = Parameter(value)

    def forward(self, x: Tensor) -> Tensor:
        return QLayerFunction.apply(  # type: ignore[no-untyped-call]
            x, self.weight, self.quantum_program, self._execute, self._post_process
        )
