from typing import Dict, List, Optional

from classiq.interface.generator.constant import Constant
from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.functions.classical_type import (
    ClassicalArray,
    ConcreteClassicalType,
)
from classiq.interface.generator.functions.port_declaration import (
    PortDeclarationDirection,
)
from classiq.interface.generator.visitor import NodeType, Visitor
from classiq.interface.model.bind_operation import BindOperation
from classiq.interface.model.classical_if import ClassicalIf
from classiq.interface.model.classical_parameter_declaration import (
    ClassicalParameterDeclaration,
)
from classiq.interface.model.control import Control
from classiq.interface.model.handle_binding import (
    HandleBinding,
    SlicedHandleBinding,
    SubscriptHandleBinding,
)
from classiq.interface.model.inplace_binary_operation import InplaceBinaryOperation
from classiq.interface.model.invert import Invert
from classiq.interface.model.model import Model
from classiq.interface.model.native_function_definition import NativeFunctionDefinition
from classiq.interface.model.port_declaration import PortDeclaration
from classiq.interface.model.power import Power
from classiq.interface.model.quantum_expressions.amplitude_loading_operation import (
    AmplitudeLoadingOperation,
)
from classiq.interface.model.quantum_expressions.arithmetic_operation import (
    ArithmeticOperation,
)
from classiq.interface.model.quantum_function_call import (
    OperandIdentifier,
    QuantumFunctionCall,
)
from classiq.interface.model.quantum_function_declaration import (
    QuantumFunctionDeclaration,
    QuantumOperandDeclaration,
)
from classiq.interface.model.quantum_lambda_function import QuantumLambdaFunction
from classiq.interface.model.quantum_type import (
    QuantumBit,
    QuantumBitvector,
    QuantumNumeric,
)
from classiq.interface.model.quantum_variable_declaration import (
    QuantumVariableDeclaration,
)
from classiq.interface.model.repeat import Repeat
from classiq.interface.model.statement_block import StatementBlock
from classiq.interface.model.variable_declaration_statement import (
    VariableDeclarationStatement,
)
from classiq.interface.model.within_apply_operation import WithinApply

from classiq import Bool, ClassicalList, Integer, Pauli, Real, Struct, StructDeclaration
from classiq.qmod.native.expression_to_qmod import transform_expression
from classiq.qmod.utilities import DEFAULT_DECIMAL_PRECISION


class DSLPrettyPrinter(Visitor):
    def __init__(
        self, decimal_precision: Optional[int] = DEFAULT_DECIMAL_PRECISION
    ) -> None:
        self._level = 0
        self._decimal_precision = decimal_precision

    def visit(self, node: NodeType) -> str:
        res = super().visit(node)
        if not isinstance(res, str):
            raise AssertionError(f"Pretty printing for {type(node)} is not supported ")
        return res

    def visit_Model(self, model: Model) -> str:
        struct_decls = [self.visit(struct_decl) for struct_decl in model.types]
        func_defs = [self.visit(func_def) for func_def in model.functions]
        constants = [self.visit(constant) for constant in model.constants]
        classical_code = (
            f"cscope ```\n{model.classical_execution_code}\n```"
            if model.classical_execution_code
            else ""
        )
        return "\n".join([*constants, *struct_decls, *func_defs, classical_code])

    def visit_Constant(self, constant: Constant) -> str:
        return f"{self._indent}{self.visit(constant.name)}: {self.visit(constant.const_type)} = {self.visit(constant.value)};\n"

    def _visit_arg_decls(self, func_def: QuantumFunctionDeclaration) -> str:
        gen_time_args = ", ".join(
            self.visit(arg_decl)
            for arg_decl in func_def.get_positional_arg_decls()
            if not isinstance(arg_decl, PortDeclaration)
        )
        quantum_args = ", ".join(
            self.visit(arg_decl)
            for arg_decl in func_def.get_positional_arg_decls()
            if isinstance(arg_decl, PortDeclaration)
        )
        gen_time_arg_list = f"<{gen_time_args}>" if gen_time_args else ""
        return f"{gen_time_arg_list}({quantum_args})"

    def visit_QuantumFunctionDeclaration(
        self, func_decl: QuantumFunctionDeclaration
    ) -> str:
        return f"qfunc {func_decl.name}{self._visit_arg_decls(func_decl)}"

    def visit_StructDeclaration(self, struct_decl: StructDeclaration) -> str:
        return f"struct {struct_decl.name} {{\n{self._visit_variables(struct_decl.variables)}}}\n"

    def _visit_variables(self, variables: Dict[str, ConcreteClassicalType]) -> str:
        self._level += 1
        variables_str = "".join(
            f"{self._indent}{self.visit(field_name)}: {self.visit(var_decl)};\n"
            for field_name, var_decl in variables.items()
        )
        self._level -= 1
        return variables_str

    def visit_QuantumVariableDeclaration(
        self, var_decl: QuantumVariableDeclaration
    ) -> str:
        return f"{var_decl.name}: {self.visit(var_decl.quantum_type)}"

    def visit_PortDeclaration(self, port_decl: PortDeclaration) -> str:
        dir_str = (
            f"{port_decl.direction} "
            if port_decl.direction != PortDeclarationDirection.Inout
            else ""
        )
        return f"{dir_str}{self.visit_QuantumVariableDeclaration(port_decl)}"

    def visit_QuantumBit(self, qtype: QuantumBit) -> str:
        return "qbit"

    def visit_QuantumBitvector(self, qtype: QuantumBitvector) -> str:
        if qtype.length is not None:
            return f"qbit[{self.visit(qtype.length)}]"
        return "qbit[]"

    def visit_QuantumNumeric(self, qtype: QuantumNumeric) -> str:
        params = ""
        if qtype.size is not None:
            assert qtype.is_signed is not None
            assert qtype.fraction_digits is not None

            params = "<{}>".format(
                ", ".join(
                    self.visit(param)
                    for param in [qtype.size, qtype.is_signed, qtype.fraction_digits]
                )
            )

        return f"qnum{params}"

    def visit_ClassicalParameterDeclaration(
        self, cparam: ClassicalParameterDeclaration
    ) -> str:
        return f"{cparam.name}: {self.visit(cparam.classical_type)}"

    def visit_Integer(self, ctint: Integer) -> str:
        return "int"

    def visit_Real(self, ctint: Real) -> str:
        return "real"

    def visit_Bool(self, ctbool: Bool) -> str:
        return "bool"

    def visit_Pauli(self, ctbool: Pauli) -> str:
        return "Pauli"

    def visit_ClassicalList(self, ctlist: ClassicalList) -> str:
        return f"{self.visit(ctlist.element_type)}[]"

    def visit_ClassicalArray(self, ctarray: ClassicalArray) -> str:
        return f"{self.visit(ctarray.element_type)}[{ctarray.size}]"

    def visit_Struct(self, struct: Struct) -> str:
        return struct.name

    def visit_VariableDeclarationStatement(
        self, local_decl: VariableDeclarationStatement
    ) -> str:
        return f"{self._indent}{self.visit_QuantumVariableDeclaration(local_decl)};\n"

    def visit_QuantumOperandDeclaration(
        self, op_decl: QuantumOperandDeclaration
    ) -> str:
        return f"{op_decl.name}: qfunc{[] if op_decl.is_list else ''} {self._visit_arg_decls(op_decl)}"

    def visit_NativeFunctionDefinition(self, func_def: NativeFunctionDefinition) -> str:
        self._level += 1
        body = "".join(self.visit(qvar_decl) for qvar_decl in func_def.body)
        self._level -= 1
        return f"{self.visit_QuantumFunctionDeclaration(func_def)} {{\n{body}}}\n"

    def visit_QuantumFunctionCall(self, func_call: QuantumFunctionCall) -> str:
        gen_time_args = ", ".join(
            self.visit(arg_decl)
            for arg_decl in func_call.get_positional_args()
            if not isinstance(arg_decl, HandleBinding)
        )
        gen_time_arg_list = f"<{gen_time_args}>" if gen_time_args else ""
        quantum_args = ", ".join(
            self.visit(arg_decl)
            for arg_decl in func_call.get_positional_args()
            if isinstance(arg_decl, HandleBinding)
        )
        return f"{self._indent}{func_call.func_name}{f'[{self.visit(func_call.function.index)}]' if isinstance(func_call.function, OperandIdentifier) else ''}{gen_time_arg_list}({quantum_args});\n"

    def visit_Control(self, op: Control) -> str:
        control = f"{self._indent}control ({self.visit(op.expression)}) {{\n"
        control += self._visit_body(op.body)
        control += f"{self._indent}}}\n"
        return control

    def visit_ClassicalIf(self, op: ClassicalIf) -> str:
        classical_if = f"{self._indent}if ({self.visit(op.condition)}) {{\n"
        if not op.then:
            raise AssertionError('Expected non empty "then" block')
        classical_if += self._visit_body(op.then)

        if op.else_:
            classical_if += f"{self._indent}}} else {{\n"
            classical_if += self._visit_body(op.else_)

        classical_if += f"{self._indent}}}\n"
        return classical_if

    def visit_WithinApply(self, op: WithinApply) -> str:
        within_apply_code = f"{self._indent}within {{\n"
        within_apply_code += self._visit_body(op.compute)
        within_apply_code += f"{self._indent}}} apply {{\n"
        within_apply_code += self._visit_body(op.action)
        within_apply_code += f"{self._indent}}}\n"
        return within_apply_code

    def visit_Repeat(self, repeat: Repeat) -> str:
        repeat_code = f"{self._indent}repeat ({self.visit(repeat.iter_var)}: {self.visit(repeat.count)}) {{\n"
        repeat_code += self._visit_body(repeat.body)
        repeat_code += f"{self._indent}}}\n"
        return repeat_code

    def visit_Power(self, power: Power) -> str:
        power_code = f"{self._indent}power ({self.visit(power.power)}) {{\n"
        power_code += self._visit_body(power.body)
        power_code += f"{self._indent}}}\n"
        return power_code

    def visit_Invert(self, invert: Invert) -> str:
        invert_code = f"{self._indent}invert {{\n"
        invert_code += self._visit_body(invert.body)
        invert_code += f"{self._indent}}}\n"
        return invert_code

    def _visit_body(self, body: StatementBlock) -> str:
        code = ""
        self._level += 1
        for statement in body:
            code += self.visit(statement)
        self._level -= 1
        return code

    def visit_InplaceBinaryOperation(self, op: InplaceBinaryOperation) -> str:
        return (
            f"{self._indent}{op.operation.value}({op.value.name}, {op.target.name});\n"
        )

    def _visit_pack_expr(self, vars: List[HandleBinding]) -> str:
        if len(vars) == 1:
            return self.visit(vars[0])

        var_list_str = ", ".join(self.visit(var) for var in vars)
        return f"{{{var_list_str}}}"

    def visit_Expression(self, expr: Expression) -> str:
        return transform_expression(
            expr.expr, level=self._level, decimal_precision=self._decimal_precision
        )

    def visit_QuantumLambdaFunction(self, qlambda: QuantumLambdaFunction) -> str:
        assert qlambda.func_decl is not None
        gen_time_args = ", ".join(
            qlambda.rename_params.get(arg_decl.name, arg_decl.name)
            for arg_decl in qlambda.func_decl.get_positional_arg_decls()
            if not isinstance(arg_decl, PortDeclaration)
        )
        quantum_args = ", ".join(
            arg_decl.name
            for arg_decl in qlambda.func_decl.get_positional_arg_decls()
            if isinstance(arg_decl, PortDeclaration)
        )
        gen_time_arg_list = f"<{gen_time_args}>" if gen_time_args else ""
        body = self._visit_body(qlambda.body)
        return f"lambda{gen_time_arg_list}({quantum_args}) {{\n{body}{self._indent}}}"

    def visit_HandleBinding(self, var_ref: HandleBinding) -> str:
        return var_ref.name

    def visit_SlicedHandleBinding(self, var_ref: SlicedHandleBinding) -> str:
        return f"{var_ref.name}[{self.visit(var_ref.start)}:{self.visit(var_ref.end)}]"

    def visit_SubscriptHandleBinding(self, var_ref: SubscriptHandleBinding) -> str:
        return f"{var_ref.name}[{self.visit(var_ref.index)}]"

    def visit_ArithmeticOperation(self, arith_op: ArithmeticOperation) -> str:
        op = "^=" if arith_op.inplace_result else "="
        return f"{self._indent}{self.visit(arith_op.result_var)} {op} {self.visit(arith_op.expression)};\n"

    def visit_AmplitudeLoadingOperation(
        self, amplitude_loading_op: AmplitudeLoadingOperation
    ) -> str:
        return f"{self._indent}{self.visit(amplitude_loading_op.result_var)} *= {self.visit(amplitude_loading_op.expression)};\n"

    def _print_bind_handles(self, handles: List[HandleBinding]) -> str:
        if len(handles) == 1:
            return self.visit(handles[0])

        return "{" + ", ".join(self.visit(handle) for handle in handles) + "}"

    def visit_BindOperation(self, bind_op: BindOperation) -> str:
        return f"{self._indent}{self._print_bind_handles(bind_op.in_handles)} -> {self._print_bind_handles(bind_op.out_handles)};\n"

    def visit_list(self, node: list) -> str:
        return "[" + ", ".join(self.visit(elem) for elem in node) + "]"

    @property
    def _indent(self) -> str:
        return "  " * self._level
