"""Classiq SDK."""

from typing import List

from classiq.interface._version import VERSION as _VERSION
from classiq.interface.generator.application_apis import *  # noqa: F403
from classiq.interface.generator.arith.register_user_input import (
    RegisterArithmeticInfo,
    RegisterUserInput,
)
from classiq.interface.generator.control_state import ControlState
from classiq.interface.generator.expressions.enums import *  # noqa: F403
from classiq.interface.generator.expressions.enums import __all__ as _enums_all
from classiq.interface.generator.functions import *  # noqa: F403
from classiq.interface.generator.functions import __all__ as _ifunc_all
from classiq.interface.generator.model import *  # noqa: F403
from classiq.interface.generator.model import __all__ as _md_all
from classiq.interface.generator.quantum_program import QuantumProgram
from classiq.interface.ide.show import show

from classiq import applications, exceptions, execution, synthesis
from classiq._internals import _qfunc_ext, logger
from classiq._internals.async_utils import (
    enable_jupyter_notebook,
    is_notebook as _is_notebook,
)
from classiq._internals.authentication.authentication import authenticate
from classiq._internals.client import configure
from classiq._internals.config import Configuration
from classiq._internals.help import open_help
from classiq.analyzer import Analyzer
from classiq.applications.chemistry import (
    construct_chemistry_model,
    molecule_problem_to_qmod,
)
from classiq.applications.combinatorial_optimization import (
    compute_qaoa_initial_point,
    construct_combinatorial_optimization_model,
    pyo_model_to_hamiltonian,
)
from classiq.applications.finance import construct_finance_model
from classiq.applications.grover import construct_grover_model
from classiq.applications.qsvm import construct_qsvm_model
from classiq.executor import (
    execute,
    execute_async,
    set_quantum_program_execution_preferences,
)
from classiq.qmod import *  # noqa: F403
from classiq.qmod import __all__ as _qmod_all
from classiq.synthesis import (
    set_constraints,
    set_execution_preferences,
    set_preferences,
    synthesize,
    synthesize_async,
)

_application_constructors_all = [
    "construct_qsvm_model",
    "construct_combinatorial_optimization_model",
    "construct_chemistry_model",
    "construct_finance_model",
    "construct_grover_model",
    "molecule_problem_to_qmod",
]

__version__ = _VERSION

if _is_notebook():
    enable_jupyter_notebook()

_sub_modules = [
    "analyzer",
    "applications",
    "exceptions",
    "execution",
    "open_help",
    "qmod",
    "synthesis",
]

__all__ = (
    [
        "RegisterUserInput",
        "RegisterArithmeticInfo",
        "ControlState",
        "Analyzer",
        "QuantumProgram",
        "authenticate",
        "synthesize",
        "synthesize_async",
        "execute",
        "execute_async",
        "set_preferences",
        "set_constraints",
        "set_execution_preferences",
        "set_quantum_program_execution_preferences",
        "show",
    ]
    + _md_all
    + _ifunc_all
    + _sub_modules
    + _application_constructors_all
    + _qmod_all
    + _enums_all
)


def __dir__() -> List[str]:
    return __all__
