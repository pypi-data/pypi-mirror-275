import sys
from abc import ABC, abstractmethod
from typing import (  # type: ignore[attr-defined]
    TYPE_CHECKING,
    Any,
    ClassVar,
    Generic,
    Optional,
    Union,
    _GenericAlias,
)

from typing_extensions import ParamSpec

from classiq.interface.ast_node import SourceReference
from classiq.interface.model.quantum_function_call import QuantumFunctionCall
from classiq.interface.model.quantum_function_declaration import (
    QuantumFunctionDeclaration,
)
from classiq.interface.model.quantum_statement import QuantumStatement
from classiq.interface.model.quantum_type import QuantumType

from classiq.qmod.qmod_parameter import CInt
from classiq.qmod.utilities import get_source_ref

if TYPE_CHECKING:
    from classiq.qmod.quantum_expandable import QTerminalCallable

P = ParamSpec("P")


class QExpandableInterface(ABC):
    @abstractmethod
    def append_statement_to_body(self, stmt: QuantumStatement) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_local_handle(self, name: str, qtype: QuantumType) -> None:
        raise NotImplementedError()


class QCallable(Generic[P], ABC):
    CURRENT_EXPANDABLE: ClassVar[Optional[QExpandableInterface]] = None
    FRAME_DEPTH = 1

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        assert QCallable.CURRENT_EXPANDABLE is not None
        source_ref = get_source_ref(sys._getframe(self.FRAME_DEPTH))
        QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
            self.create_quantum_function_call(source_ref, *args, **kwargs)
        )
        return

    @property
    @abstractmethod
    def func_decl(self) -> QuantumFunctionDeclaration:
        raise NotImplementedError

    # Support comma-separated generic args in older Python versions
    if sys.version_info[0:2] < (3, 10):

        def __class_getitem__(cls, args) -> _GenericAlias:
            return _GenericAlias(cls, args)

    @abstractmethod
    def create_quantum_function_call(
        self, source_ref_: SourceReference, *args: Any, **kwargs: Any
    ) -> QuantumFunctionCall:
        raise NotImplementedError()


class QCallableList(QCallable, Generic[P], ABC):
    if TYPE_CHECKING:

        @property
        def len(self) -> int: ...

        def __getitem__(self, key: Union[slice, int, CInt]) -> "QTerminalCallable":
            raise NotImplementedError()
