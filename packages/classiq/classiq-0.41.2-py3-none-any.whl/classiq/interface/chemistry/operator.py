from functools import reduce
from typing import Any, Collection, Dict, List, Optional, Tuple, Union, cast

import numpy as np
import pydantic
import sympy
from more_itertools import all_equal

from classiq.interface.generator.expressions.enums.pauli import Pauli
from classiq.interface.generator.function_params import validate_expression_str
from classiq.interface.generator.parameters import (
    ParameterComplexType,
    ParameterType,
    PydanticParameterComplexType,
)
from classiq.interface.helpers.custom_pydantic_types import (
    PydanticPauliList,
    PydanticPauliMonomial,
    PydanticPauliMonomialStr,
)
from classiq.interface.helpers.hashable_pydantic_base_model import (
    HashablePydanticBaseModel,
)
from classiq.interface.helpers.versioned_model import VersionedModel

from classiq.exceptions import ClassiqValueError


class PauliOperator(HashablePydanticBaseModel, VersionedModel):
    """
    Specification of a Pauli sum operator.
    """

    pauli_list: PydanticPauliList = pydantic.Field(
        description="A list of tuples each containing a pauli string comprised of I,X,Y,Z characters and a complex coefficient; for example [('IZ', 0.1), ('XY', 0.2)].",
    )
    is_hermitian: bool = pydantic.Field(default=False)
    has_complex_coefficients: bool = pydantic.Field(default=True)

    def show(self) -> str:
        if self.is_hermitian:
            # If the operator is hermitian then the coefficients must be numeric
            return "\n".join(
                f"{summand[1].real:+.3f} * {summand[0]}" for summand in self.pauli_list  # type: ignore[union-attr]
            )
        return "\n".join(
            f"+({summand[1]:+.3f}) * {summand[0]}" for summand in self.pauli_list
        )

    @pydantic.validator("pauli_list", each_item=True, pre=True)
    def _validate_pauli_monomials(
        cls, monomial: Tuple[PydanticPauliMonomialStr, ParameterComplexType]
    ) -> Tuple[PydanticPauliMonomialStr, ParameterComplexType]:
        _PauliMonomialLengthValidator(  # type: ignore[call-arg]
            monomial=monomial
        )  # Validate the length of the monomial.
        coeff = cls._validate_monomial_coefficient(monomial[1])
        parsed_monomial = _PauliMonomialParser(string=monomial[0], coeff=coeff)  # type: ignore[call-arg]
        return (parsed_monomial.string, parsed_monomial.coeff)

    @staticmethod
    def _validate_monomial_coefficient(
        coeff: Union[sympy.Expr, ParameterComplexType]
    ) -> ParameterComplexType:
        if isinstance(coeff, str):
            validate_expression_str(coeff)
        elif isinstance(coeff, sympy.Expr):
            coeff = str(coeff)
        return coeff

    @pydantic.validator("pauli_list")
    def _validate_pauli_list(cls, pauli_list: PydanticPauliList) -> PydanticPauliList:
        if not all_equal(len(summand[0]) for summand in pauli_list):
            raise ClassiqValueError("Pauli strings have incompatible lengths.")
        return pauli_list

    @pydantic.root_validator
    def _validate_hermitianity(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        pauli_list = values.get("pauli_list", [])
        if all(isinstance(summand[1], complex) for summand in pauli_list):
            values["is_hermitian"] = all(
                np.isclose(complex(summand[1]).real, summand[1])
                for summand in pauli_list
            )
        if values.get("is_hermitian", False):
            values["has_complex_coefficients"] = False
            values["pauli_list"] = [
                (summand[0], complex(summand[1].real)) for summand in pauli_list
            ]
        else:
            values["has_complex_coefficients"] = not all(
                np.isclose(complex(summand[1]).real, summand[1])
                for summand in pauli_list
                if isinstance(summand[1], complex)
            )
        return values

    def __mul__(self, coefficient: complex) -> "PauliOperator":
        multiplied_ising = [
            (monomial[0], self._multiply_monomial_coefficient(monomial[1], coefficient))
            for monomial in self.pauli_list
        ]
        return self.__class__(pauli_list=multiplied_ising)

    @staticmethod
    def _multiply_monomial_coefficient(
        monomial_coefficient: ParameterComplexType, coefficient: complex
    ) -> ParameterComplexType:
        if isinstance(monomial_coefficient, ParameterType):
            return str(sympy.sympify(monomial_coefficient) * coefficient)
        return monomial_coefficient * coefficient

    @property
    def is_commutative(self) -> bool:
        return all(
            self._is_sub_pauli_commutative(
                [summand[0][qubit_num] for summand in self.pauli_list]
            )
            for qubit_num in range(self.num_qubits)
        )

    @staticmethod
    def _is_sub_pauli_commutative(qubit_pauli_string: Union[List[str], str]) -> bool:
        unique_paulis = set(qubit_pauli_string) - {"I"}
        return len(unique_paulis) <= 1

    @property
    def num_qubits(self) -> int:
        return len(self.pauli_list[0][0])

    def to_matrix(self) -> np.ndarray:
        if not all(isinstance(summand[1], complex) for summand in self.pauli_list):
            raise ClassiqValueError(
                "Supporting only Hamiltonian with numeric coefficients."
            )
        return sum(
            cast(complex, summand[1]) * to_pauli_matrix(summand[0])
            for summand in self.pauli_list
        )  # type: ignore[return-value]

    @staticmethod
    def _extend_pauli_string(
        pauli_string: PydanticPauliMonomialStr, num_extra_qubits: int
    ) -> PydanticPauliMonomialStr:
        return "I" * num_extra_qubits + pauli_string

    def extend(self, num_extra_qubits: int) -> "PauliOperator":
        new_pauli_list = [
            (self._extend_pauli_string(pauli_string, num_extra_qubits), coeff)
            for (pauli_string, coeff) in self.pauli_list
        ]
        return self.copy(update={"pauli_list": new_pauli_list}, deep=True)

    @staticmethod
    def _reorder_pauli_string(
        pauli_string: PydanticPauliMonomialStr,
        order: Collection[int],
        new_num_qubits: int,
    ) -> PydanticPauliMonomialStr:
        reversed_pauli_string = pauli_string[::-1]
        reversed_new_pauli_string = ["I"] * new_num_qubits

        for logical_pos, actual_pos in enumerate(order):
            reversed_new_pauli_string[actual_pos] = reversed_pauli_string[logical_pos]

        return "".join(reversed(reversed_new_pauli_string))

    @staticmethod
    def _validate_reorder(
        order: Collection[int],
        num_qubits: int,
        num_extra_qubits: int,
    ) -> None:
        if num_extra_qubits < 0:
            raise ClassiqValueError("Number of extra qubits cannot be negative")

        if len(order) != num_qubits:
            raise ClassiqValueError("The qubits order doesn't match the Pauli operator")

        if len(order) != len(set(order)):
            raise ClassiqValueError("The qubits order is not one-to-one")

        if not all(pos < num_qubits + num_extra_qubits for pos in order):
            raise ClassiqValueError(
                "The qubits order contains qubits which do no exist"
            )

    @classmethod
    def reorder(
        cls,
        operator: "PauliOperator",
        order: Collection[int],
        num_extra_qubits: int = 0,
    ) -> "PauliOperator":
        cls._validate_reorder(order, operator.num_qubits, num_extra_qubits)

        new_num_qubits = operator.num_qubits + num_extra_qubits
        new_pauli_list = [
            (cls._reorder_pauli_string(pauli_string, order, new_num_qubits), coeff)
            for pauli_string, coeff in operator.pauli_list
        ]
        return cls(pauli_list=new_pauli_list)

    @classmethod
    def from_unzipped_lists(
        cls,
        operators: List[List[Pauli]],
        coefficients: Optional[List[complex]] = None,
    ) -> "PauliOperator":
        if coefficients is None:
            coefficients = [1] * len(operators)

        if len(operators) != len(coefficients):
            raise ClassiqValueError(
                f"The number of coefficients ({len(coefficients)}) must be equal to the number of pauli operators ({len(operators)})"
            )

        return cls(
            pauli_list=[
                (pauli_integers_to_str(op), coeff)
                for op, coeff in zip(operators, coefficients)
            ]
        )

    class Config:
        frozen = True


class PauliOperatorV1(HashablePydanticBaseModel):
    """
    Specification of a Pauli sum operator.
    """

    pauli_list: PydanticPauliList = pydantic.Field(
        description="A list of tuples each containing a pauli string comprised of I,X,Y,Z characters and a complex coefficient; for example [('IZ', 0.1), ('XY', 0.2)].",
    )
    is_hermitian: bool = pydantic.Field(default=False)
    has_complex_coefficients: bool = pydantic.Field(default=True)

    def show(self) -> str:
        if self.is_hermitian:
            # If the operator is hermitian then the coefficients must be numeric
            return "\n".join(
                f"{summand[1].real:+.3f} * {summand[0]}" for summand in self.pauli_list  # type: ignore[union-attr]
            )
        return "\n".join(
            f"+({summand[1]:+.3f}) * {summand[0]}" for summand in self.pauli_list
        )

    @pydantic.validator("pauli_list", each_item=True, pre=True)
    def _validate_pauli_monomials(
        cls, monomial: Tuple[PydanticPauliMonomialStr, ParameterComplexType]
    ) -> Tuple[PydanticPauliMonomialStr, ParameterComplexType]:
        _PauliMonomialLengthValidator(  # type: ignore[call-arg]
            monomial=monomial
        )  # Validate the length of the monomial.
        coeff = cls._validate_monomial_coefficient(monomial[1])
        parsed_monomial = _PauliMonomialParser(string=monomial[0], coeff=coeff)  # type: ignore[call-arg]
        return (parsed_monomial.string, parsed_monomial.coeff)

    @staticmethod
    def _validate_monomial_coefficient(
        coeff: Union[sympy.Expr, ParameterComplexType]
    ) -> ParameterComplexType:
        if isinstance(coeff, str):
            validate_expression_str(coeff)
        elif isinstance(coeff, sympy.Expr):
            coeff = str(coeff)
        return coeff

    @pydantic.validator("pauli_list")
    def _validate_pauli_list(cls, pauli_list: PydanticPauliList) -> PydanticPauliList:
        if not all_equal(len(summand[0]) for summand in pauli_list):
            raise ClassiqValueError("Pauli strings have incompatible lengths.")
        return pauli_list

    @pydantic.root_validator
    def _validate_hermitianity(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        pauli_list = values.get("pauli_list", [])
        if all(isinstance(summand[1], complex) for summand in pauli_list):
            values["is_hermitian"] = all(
                np.isclose(complex(summand[1]).real, summand[1])
                for summand in pauli_list
            )
        if values.get("is_hermitian", False):
            values["has_complex_coefficients"] = False
            values["pauli_list"] = [
                (summand[0], complex(summand[1].real)) for summand in pauli_list
            ]
        else:
            values["has_complex_coefficients"] = not all(
                np.isclose(complex(summand[1]).real, summand[1])
                for summand in pauli_list
                if isinstance(summand[1], complex)
            )
        return values

    def __mul__(self, coefficient: complex) -> "PauliOperatorV1":
        multiplied_ising = [
            (monomial[0], self._multiply_monomial_coefficient(monomial[1], coefficient))
            for monomial in self.pauli_list
        ]
        return self.__class__(pauli_list=multiplied_ising)

    @staticmethod
    def _multiply_monomial_coefficient(
        monomial_coefficient: ParameterComplexType, coefficient: complex
    ) -> ParameterComplexType:
        if isinstance(monomial_coefficient, ParameterType):
            return str(sympy.sympify(monomial_coefficient) * coefficient)
        return monomial_coefficient * coefficient

    @property
    def is_commutative(self) -> bool:
        return all(
            self._is_sub_pauli_commutative(
                [summand[0][qubit_num] for summand in self.pauli_list]
            )
            for qubit_num in range(self.num_qubits)
        )

    @staticmethod
    def _is_sub_pauli_commutative(qubit_pauli_string: Union[List[str], str]) -> bool:
        unique_paulis = set(qubit_pauli_string) - {"I"}
        return len(unique_paulis) <= 1

    @property
    def num_qubits(self) -> int:
        return len(self.pauli_list[0][0])

    def to_matrix(self) -> np.ndarray:
        if not all(isinstance(summand[1], complex) for summand in self.pauli_list):
            raise ClassiqValueError(
                "Supporting only Hamiltonian with numeric coefficients."
            )
        return sum(
            cast(complex, summand[1]) * to_pauli_matrix(summand[0])
            for summand in self.pauli_list
        )  # type: ignore[return-value]

    @staticmethod
    def _extend_pauli_string(
        pauli_string: PydanticPauliMonomialStr, num_extra_qubits: int
    ) -> PydanticPauliMonomialStr:
        return "I" * num_extra_qubits + pauli_string

    def extend(self, num_extra_qubits: int) -> "PauliOperatorV1":
        new_pauli_list = [
            (self._extend_pauli_string(pauli_string, num_extra_qubits), coeff)
            for (pauli_string, coeff) in self.pauli_list
        ]
        return self.copy(update={"pauli_list": new_pauli_list}, deep=True)

    @staticmethod
    def _reorder_pauli_string(
        pauli_string: PydanticPauliMonomialStr,
        order: Collection[int],
        new_num_qubits: int,
    ) -> PydanticPauliMonomialStr:
        reversed_pauli_string = pauli_string[::-1]
        reversed_new_pauli_string = ["I"] * new_num_qubits

        for logical_pos, actual_pos in enumerate(order):
            reversed_new_pauli_string[actual_pos] = reversed_pauli_string[logical_pos]

        return "".join(reversed(reversed_new_pauli_string))

    @staticmethod
    def _validate_reorder(
        order: Collection[int],
        num_qubits: int,
        num_extra_qubits: int,
    ) -> None:
        if num_extra_qubits < 0:
            raise ClassiqValueError("Number of extra qubits cannot be negative")

        if len(order) != num_qubits:
            raise ClassiqValueError("The qubits order doesn't match the Pauli operator")

        if len(order) != len(set(order)):
            raise ClassiqValueError("The qubits order is not one-to-one")

        if not all(pos < num_qubits + num_extra_qubits for pos in order):
            raise ClassiqValueError(
                "The qubits order contains qubits which do no exist"
            )

    @classmethod
    def reorder(
        cls,
        operator: "PauliOperatorV1",
        order: Collection[int],
        num_extra_qubits: int = 0,
    ) -> "PauliOperatorV1":
        cls._validate_reorder(order, operator.num_qubits, num_extra_qubits)

        new_num_qubits = operator.num_qubits + num_extra_qubits
        new_pauli_list = [
            (cls._reorder_pauli_string(pauli_string, order, new_num_qubits), coeff)
            for pauli_string, coeff in operator.pauli_list
        ]
        return cls(pauli_list=new_pauli_list)

    @classmethod
    def from_unzipped_lists(
        cls,
        operators: List[List[Pauli]],
        coefficients: Optional[List[complex]] = None,
    ) -> "PauliOperatorV1":
        if coefficients is None:
            coefficients = [1] * len(operators)

        if len(operators) != len(coefficients):
            raise ClassiqValueError(
                f"The number of coefficients ({len(coefficients)}) must be equal to the number of pauli operators ({len(operators)})"
            )

        return cls(
            pauli_list=[
                (pauli_integers_to_str(op), coeff)
                for op, coeff in zip(operators, coefficients)
            ]
        )

    class Config:
        frozen = True


# This class validates the length of a monomial.
@pydantic.dataclasses.dataclass
class _PauliMonomialLengthValidator:
    monomial: PydanticPauliMonomial


@pydantic.dataclasses.dataclass
class _PauliMonomialParser:
    string: PydanticPauliMonomialStr
    coeff: PydanticParameterComplexType


_PAULI_MATRICES = {
    "I": np.array([[1, 0], [0, 1]]),
    "X": np.array([[0, 1], [1, 0]]),
    "Y": np.array([[0, -1j], [1j, 0]]),
    "Z": np.array([[1, 0], [0, -1]]),
}


def to_pauli_matrix(pauli_op: PydanticPauliMonomialStr) -> np.ndarray:
    return reduce(np.kron, [_PAULI_MATRICES[pauli] for pauli in reversed(pauli_op)])


def validate_operator_is_hermitian(pauli_operator: PauliOperator) -> PauliOperator:
    if not pauli_operator.is_hermitian:
        raise ClassiqValueError("Coefficients of the Hamiltonian must be real numbers")
    return pauli_operator


def validate_operator_has_no_complex_coefficients(
    pauli_operator: PauliOperator,
) -> PauliOperator:
    if pauli_operator.has_complex_coefficients:
        raise ClassiqValueError(
            "Coefficients of the Hamiltonian mustn't be complex numbers"
        )
    return pauli_operator


def pauli_integers_to_str(paulis: List[Pauli]) -> str:
    return "".join([Pauli(pauli).name for pauli in paulis])


class PauliOperators(VersionedModel):
    operators: List[PauliOperator]
