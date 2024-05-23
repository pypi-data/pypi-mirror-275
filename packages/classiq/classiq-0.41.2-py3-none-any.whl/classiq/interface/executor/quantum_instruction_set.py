from classiq._internals.enum_utils import StrEnum
from classiq.exceptions import ClassiqValueError


class QuantumInstructionSet(StrEnum):
    QASM = "qasm"
    QSHARP = "qsharp"
    IONQ = "ionq"

    @classmethod
    def from_suffix(cls, suffix: str) -> "QuantumInstructionSet":
        if suffix == "qasm":
            return QuantumInstructionSet.QASM
        if suffix == "qs":
            return QuantumInstructionSet.QSHARP
        if suffix == "ionq":
            return QuantumInstructionSet.IONQ
        raise ClassiqValueError("Illegal suffix")
