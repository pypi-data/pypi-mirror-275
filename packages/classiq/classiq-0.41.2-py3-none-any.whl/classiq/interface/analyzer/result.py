from typing import Dict, List, Literal, Optional, Set, Tuple, Union
from uuid import UUID

import pydantic
from pydantic import Field
from typing_extensions import Annotated

from classiq.interface.helpers.custom_pydantic_types import PydanticNonEmptyString
from classiq.interface.helpers.versioned_model import VersionedModel

from classiq._internals.enum_utils import StrEnum
from classiq.exceptions import ClassiqValueError

Match = List[List[int]]


class GraphStatus(StrEnum):
    SUCCESS = "success"
    ERROR = "error"


class GraphResult(VersionedModel):
    kind: Literal["graph"] = Field(default="graph")
    details: str


class RbResults(VersionedModel):
    mean_fidelity: float
    average_error: float
    A: float
    B: float
    success_probability: List[float]
    parameters_error: Tuple[float, ...]


class DataID(pydantic.BaseModel):
    id: UUID


class QasmCode(pydantic.BaseModel):
    code: str


class AnalysisStatus(StrEnum):
    NONE = "none"
    SUCCESS = "success"
    CANCELLED = "cancelled"
    ERROR = "error"


class BasisGates(StrEnum):
    CX = "cx"
    CY = "cy"
    CZ = "cz"
    U = "u"
    U2 = "u2"
    P = "p"


class HardwareComparisonInformation(pydantic.BaseModel):
    devices: List[str] = pydantic.Field(
        default=..., description="Device which is used for the transpilation."
    )
    providers: List[str] = pydantic.Field(
        default=..., description="Provider cloud of the device."
    )
    depth: List[pydantic.NonNegativeInt] = pydantic.Field(
        default=..., description="Circuit depth."
    )
    multi_qubit_gate_count: List[pydantic.NonNegativeInt] = pydantic.Field(
        default=..., description="Number of multi qubit gates."
    )
    total_gate_count: List[pydantic.NonNegativeInt] = pydantic.Field(
        default=..., description="Number of total gates."
    )

    @pydantic.root_validator
    def validate_equal_length(cls, values: Dict[str, list]) -> Dict[str, list]:
        lengths = list(map(len, values.values()))
        if len(set(lengths)) != 1:
            raise ClassiqValueError("All lists should have the same length")
        return values


# TODO: copy the types for `devices` & `providers` from `HardwareComparisonInformation`
#   Once https://github.com/Classiq-Technologies/Cadmium/pull/10069 is resolved
class SingleHardwareInformation(pydantic.BaseModel):
    devices: str = pydantic.Field(
        default=..., description="Device which is used for the transpilation."
    )
    providers: str = pydantic.Field(
        default=..., description="Provider cloud of the device."
    )
    depth: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Circuit depth."
    )
    multi_qubit_gate_count: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of multi qubit gates."
    )
    total_gate_count: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of total gates."
    )


class HardwareComparisonData(VersionedModel):
    kind: Literal["hardware_comparison"] = Field(default="hardware_comparison")
    data: List[SingleHardwareInformation]


HardwareComparisonGraphType = Annotated[
    Union[HardwareComparisonData, GraphResult], Field(discriminator="kind")
]

_HARDWARE_COMPARISON_TABLE_COLUMNS_NAMES: Dict[str, str] = {
    s.upper(): s.capitalize() for s in SingleHardwareInformation.__fields__
}


class HardwareComparisonDataColumns(pydantic.BaseModel):
    columns: Dict[str, str] = _HARDWARE_COMPARISON_TABLE_COLUMNS_NAMES


class AvailableHardware(pydantic.BaseModel):
    ibm_quantum: Optional[Dict[PydanticNonEmptyString, bool]] = pydantic.Field(
        default=None,
        description="available IBM Quantum devices with boolean indicates if a given device has enough qubits.",
    )
    azure_quantum: Optional[Dict[PydanticNonEmptyString, bool]] = pydantic.Field(
        default=None,
        description="available Azure Quantum devices with boolean indicates if a given device has enough qubits.",
    )
    amazon_braket: Optional[Dict[PydanticNonEmptyString, bool]] = pydantic.Field(
        default=None,
        description="available Amazon Braket devices with boolean indicates if a given device has enough qubits.",
    )


class DevicesResult(VersionedModel):
    devices: AvailableHardware
    status: GraphStatus


class QuantumCircuitProperties(pydantic.BaseModel):
    depth: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Circuit depth"
    )
    auxiliary_qubits: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of Auxiliary qubits"
    )
    classical_bits: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of classical bits"
    )
    gates_count: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Total number of gates in the circuit"
    )
    multi_qubit_gates_count: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of multi-qubit gates in circuit"
    )
    non_entangled_subcircuits_count: pydantic.NonNegativeInt = pydantic.Field(
        default=..., description="Number of non-entangled sub-circuit "
    )


class NativeQuantumCircuitProperties(QuantumCircuitProperties):
    native_gates: Set[BasisGates] = pydantic.Field(
        default=..., description="Native gates used for decomposition"
    )


class Circuit(pydantic.BaseModel):
    closed_circuit_qasm: str


class Analysis(VersionedModel):
    input_properties: QuantumCircuitProperties = pydantic.Field(
        default=..., description="Input circuit properties"
    )
    native_properties: NativeQuantumCircuitProperties = pydantic.Field(
        default=..., description="Transpiled circuit properties"
    )
