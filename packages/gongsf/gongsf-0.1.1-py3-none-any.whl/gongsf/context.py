from __future__ import annotations
from typing import TYPE_CHECKING
import ctypes as ct
from .lib import gsf, c_str
if TYPE_CHECKING:
    from .data import Schema, Class


class Context:
    def __init__(self, handle, const: bool = True, *, own: bool = False) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const and not own
        self._own = own

    @classmethod
    def new(cls) -> Context:
        return Context(gsf.context_new(), own=True)

    def __del__(self) -> None:
        if self._own:
            gsf.delete_context[None](self.handle)

    def import_schema(self, schema: Schema) -> None:
        gsf.context_import_schema(self.handle, schema.handle)

    def add_class(self, class_: Class) -> None:
        gsf.context_add_class(self.handle, class_.handle)

    def class_by_name(self, name: str) -> Class:
        return Class(gsf.context_add_class(self.handle, c_str(name)))
