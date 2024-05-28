from __future__ import annotations
from typing import TYPE_CHECKING
import ctypes as ct
from .lib import gsf, c_str, c_str_or, py_str, gsf_raise
if TYPE_CHECKING:
    from .context import Context
    from .data import Class


class Typing:
    def __init__(self, handle) -> None:
        self.handle = ct.c_void_p(handle)

    def __str__(self) -> str:
        return Typing.to_string(self)

    @classmethod
    def to_string(cls, typing: Typing, max_size: int = 128) -> str:
        return py_str(gsf.typing_to_string[ct.c_char_p](typing.handle))

    @property
    def type_count(self) -> int:
        return gsf.typing_type_count[ct.c_size_t](self.handle)

    def with_type(self, type_: Type | str, is_default: bool = False) -> Typing:
        return Typing(gsf.typing_with_type(self.handle, c_str_or(type_, lambda t: t.handle), ct.c_int(is_default)))

    def get_type(self, index: int) -> Type:
        return Type(gsf.typing_get_type(self.handle, ct.c_size_t(index)))

    @property
    def default(self) -> Type:
        return Type(gsf.typing_get_default(self.handle))

    def with_default(self, index: int) -> Typing:
        return Typing(gsf.typing_with_default(self.handle, ct.c_size_t(index)))

    def without_default(self) -> Typing:
        return Typing(gsf.typing_without_default(self.handle))

    def matches_type(self, preset: Type) -> Type | None:
        found = ct.c_void_p()
        result = gsf.typing_match_type[ct.c_int](self.handle, preset.handle, ct.pointer(found))
        if result > 0:
            return Type(found)
        elif result == 0:
            return None
        gsf_raise()


class Type:
    def __init__(self, handle, const: bool = True, *, own: bool = False) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const and not own
        self._own = own

    def __del__(self) -> None:
        if self._own:
            gsf.delete_type[None](self.handle)

    def __str__(self) -> str:
        return Type.to_string(self)

    @classmethod
    def from_string(cls, string: str, ctx: Context | None) -> Type:
        result = Type(gsf.create_typing(), own=True)
        gsf.type_from_string(result.handle, c_str(string), ctx.handle)
        return result

    @classmethod
    def to_string(cls, type_: Type, max_size: int = 128) -> str:
        string = ' ' * max_size
        return py_str(gsf.type_to_string[ct.c_char_p](c_str(string), max_size, type_.handle))

    def matches(self, preset: Type, strict: bool = False) -> bool:
        func = gsf.type_matches
        if strict:
            func = gsf.type_matches_strict
        return func(self.handle, preset.handle)

    def is_null(self) -> bool:
        return gsf.type_is_null[ct.c_bool](self.handle)

    def is_primitive(self) -> bool:
        return gsf.type_is_primitive[ct.c_bool](self.handle)

    def is_string(self) -> bool:
        return gsf.type_is_string[ct.c_bool](self.handle)

    def is_scalar(self) -> bool:
        return gsf.type_is_scalar[ct.c_bool](self.handle)

    def is_int(self) -> bool:
        return gsf.type_is_int[ct.c_bool](self.handle)

    def is_uint(self) -> bool:
        return gsf.type_is_uint[ct.c_bool](self.handle)

    def is_float(self) -> bool:
        return gsf.type_is_primitive[ct.c_bool](self.handle)

    def is_enum(self) -> bool:
        return gsf.type_is_primitive[ct.c_bool](self.handle)

    def is_container(self) -> bool:
        return gsf.type_is_container[ct.c_bool](self.handle)

    def is_collection(self) -> bool:
        return gsf.type_is_collection[ct.c_bool](self.handle)

    def is_array(self) -> bool:
        return gsf.type_is_array[ct.c_bool](self.handle)

    def is_list(self) -> bool:
        return gsf.type_is_list[ct.c_bool](self.handle)

    def is_map(self) -> bool:
        return gsf.type_is_map[ct.c_bool](self.handle)

    def is_object(self) -> bool:
        return gsf.type_is_object[ct.c_bool](self.handle)

    def get_element_type(self) -> Type:
        return Type(gsf.type_get_element_type(self.handle))

    def get_element_typing(self) -> Typing:
        return Typing(gsf.type_get_element_typing(self.handle))

    def get_object_class(self) -> Class:
        return Class(gsf.type_get_object_class(self.handle))

    # def get_enum(self) -> Enum:
    #     return Enum(gsf.type_get_object_class(self.handle))
