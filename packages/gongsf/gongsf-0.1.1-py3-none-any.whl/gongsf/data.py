from __future__ import annotations
from typing import Iterable
import ctypes as ct
from .types import Typing, Type
from .context import Context
from .lib import gsf, c_str, c_str_or, py_str


class Descriptor:
    def __init__(self, handle, const: bool = True, *, own: bool = False) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const and not own
        self._own = own

    @classmethod
    def new(cls, group: str, name: str, version: str) -> Descriptor:
        handle = gsf.descriptor_new(c_str(group), c_str(name), c_str(version))
        return Descriptor(handle, own=True)

    def __del__(self) -> None:
        if self._own:
            gsf.delete_descriptor[None](self.handle)

    @property
    def const(self) -> bool:
        return self._const

    def edit(self, group: str | None, name: str | None, version: str | None) -> None:
        gsf.descriptor_edit(self.handle, c_str(group), c_str(name), c_str(version))

    @property
    def group(self) -> str:
        return py_str(gsf.descriptor_get_group[ct.c_char_p](self.handle))

    @group.setter
    def group(self, value: str) -> None:
        self.edit(value, None, None)

    @property
    def name(self) -> str:
        return py_str(gsf.descriptor_get_name[ct.c_char_p](self.handle))

    @name.setter
    def name(self, value: str) -> None:
        self.edit(None, value, None)

    @property
    def version(self) -> str:
        return py_str(gsf.descriptor_get_version[ct.c_char_p](self.handle))

    @version.setter
    def version(self, value: str) -> None:
        self.edit(None, None, value)


class Schema:
    def __init__(self, handle, const: bool = True, own: bool = False, descriptor: Descriptor | None = None) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const and not own
        self._own = own
        self._descriptor = descriptor

    @classmethod
    def new(cls, descriptor: Descriptor, root: Typing | str, class_count: int) -> Schema:
        return Schema(
            gsf.schema_new(descriptor.handle, c_str_or(root, lambda t: t.handle), ct.c_size_t(class_count)),
            False, True, descriptor
        )

    def __del__(self) -> None:
        if self._own:
            gsf.delete_schema[None](self.handle)

    @property
    def const(self) -> bool:
        return self._const

    def import_other(self, schema: Schema) -> None:
        gsf.schema_import_other(self.handle, schema.handle)

    @property
    def descriptor(self) -> Descriptor:
        return Descriptor(gsf.schema_get_descriptor(self.handle))

    @descriptor.setter
    def descriptor(self, value: Descriptor) -> None:
        gsf.schema_set_descriptor(value.handle)

    @property
    def context(self) -> Context:
        return Context(gsf.schema_get_context(self.handle))

    @property
    def root(self) -> Typing:
        return Typing(gsf.schema_get_root(self.handle))

    @root.setter
    def root(self, value: Typing) -> None:
        gsf.schema_set_root(self.handle, value.handle)

    @property
    def class_count(self) -> int:
        return gsf.schema_class_count[ct.c_size_t](self.handle)

    def add_class(self, name: str, label_count: int) -> Class:
        return Class(gsf.schema_add_class(self.handle, c_str(name), ct.c_size_t(label_count)), False)

    def get_class(self, index: int) -> Class:
        return Class(gsf.schema_get_class(self.handle, ct.c_size_t(index)), self._const)

    def remove_class(self, index: int) -> None:
        gsf.schema_remove_class(self.handle, index)


class Class:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const

    @property
    def const(self) -> bool:
        return self._const

    @property
    def name(self) -> str:
        return py_str(gsf.class_get_name[ct.c_char_p](self.handle))

    @name.setter
    def name(self, value: str):
        gsf.class_set_name(self.handle, c_str(value))

    @property
    def label_count(self) -> int:
        return gsf.class_label_count[ct.c_size_t](self.handle)

    def add_label(self, key: str, typing: Typing | str) -> Label:
        return Label(gsf.class_add_label(self.handle, c_str(key), c_str_or(typing, lambda t: t.handle)), False)

    def get_label(self, index: int) -> Label:
        return Label(gsf.class_get_label(self.handle, ct.c_size_t(index)), self._const)

    def remove_label(self, index: int) -> None:
        gsf.class_remove_label(self.handle, index)

    def index_at_label(self, label: Label) -> int:
        return gsf.class_index_at_label[ct.c_size_t](self.handle, label.handle)

    def index_at_key(self, key: str) -> int:
        return gsf.class_index_at_key[ct.c_size_t](self.handle, c_str(key))


class Label:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const

    @property
    def const(self) -> bool:
        return self._const

    @property
    def key(self) -> str:
        return py_str(gsf.label_get_key[ct.c_char_p](self.handle))

    @key.setter
    def key(self, value: str):
        gsf.label_set_key(self.handle, c_str(value))

    @property
    def typing(self) -> Typing:
        return Typing(gsf.label_get_typing(self.handle))

    @typing.setter
    def typing(self, value: Typing | str):
        gsf.label_set_typing(self.handle, c_str_or(value, lambda t: t.handle))

    @property
    def doc(self) -> str:
        return py_str(gsf.label_get_doc[ct.c_char_p](self.handle))

    @doc.setter
    def doc(self, value: str):
        gsf.label_set_key(self.handle, c_str(value))


class Article:
    def __init__(self, handle, const: bool = True, own: bool = False) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const and not own
        self._own = own

    @property
    def const(self) -> bool:
        return self._const

    @classmethod
    def new(cls, schema: Schema) -> Article:
        if not schema.const:
            handle = gsf.article_new(schema.handle)
        else:
            handle = gsf.article_new_const_schema(schema.handle)
        return Article(handle, own=True)

    def __del__(self) -> None:
        if self._own:
            gsf.delete_article[None](self.handle)

    @property
    def schema(self) -> Schema:
        return Schema(gsf.article_get_schema(self.handle))

    @property
    def root(self) -> Value:
        return Value(gsf.article_access_root(self.handle), self.const)


class Object:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const

    @property
    def const(self) -> bool:
        return self._const

    def __getitem__(self, name: str) -> Value:
        return self.at_key(name)

    def get_class(self) -> Class:
        return Class(gsf.object_get_class(self.handle))

    def at_label(self, label: Label) -> Value:
        return Value(gsf.object_access_at_label(self.handle, label.handle), self.const)

    def at_key(self, key: str) -> Value:
        return Value(gsf.object_access_at_key(self.handle, c_str(key)), self.const)

    def apply_defaults(self) -> int:
        return gsf.object_apply_defaults[ct.c_size_t](self.handle)


class Array:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = handle
        self._const = const

    @property
    def const(self) -> bool:
        return self._const

    @property
    def type(self) -> Type:
        return Type(gsf.array_get_type(self.handle))

    @property
    def size(self) -> int:
        return gsf.array_get_size[ct.c_size_t](self.handle)

    @size.setter
    def size(self, value: int) -> None:
        gsf.array_resize(self.handle, ct.c_size_t(value))

    @property
    def i8(self) -> ct.pointer[ct.c_int8]:
        return gsf.array_as_i8[ct.POINTER(ct.c_int8)]()

    @property
    def i16(self) -> ct.pointer[ct.c_int16]:
        return gsf.array_as_i16[ct.POINTER(ct.c_int16)]()

    @property
    def i32(self) -> ct.pointer[ct.c_int32]:
        return gsf.array_as_i32[ct.POINTER(ct.c_int32)]()

    @property
    def i64(self) -> ct.pointer[ct.c_int64]:
        return gsf.array_as_i64[ct.POINTER(ct.c_int64)]()

    @property
    def u8(self) -> ct.pointer[ct.c_uint8]:
        return gsf.array_as_u8[ct.POINTER(ct.c_uint8)]()

    @property
    def u16(self) -> ct.pointer[ct.c_uint16]:
        return gsf.array_as_u16[ct.POINTER(ct.c_uint16)]()

    @property
    def u32(self) -> ct.pointer[ct.c_uint32]:
        return gsf.array_as_u32[ct.POINTER(ct.c_uint32)]()

    @property
    def u64(self) -> ct.pointer[ct.c_uint64]:
        return gsf.array_as_u64[ct.POINTER(ct.c_uint64)]()

    @property
    def f32(self) -> ct.pointer[ct.c_float]:
        return gsf.array_as_f32[ct.POINTER(ct.c_float)]()

    @property
    def f64(self) -> ct.pointer[ct.c_double]:
        return gsf.array_as_f64[ct.POINTER(ct.c_double)]()


class List:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const
        self._iter: int = -1

    @property
    def const(self) -> bool:
        return self._const

    def __bool__(self) -> bool:
        return len(self) > 0

    def __iter__(self) -> List:
        self._iter = -1
        return self

    def __next__(self) -> Value:
        self._iter += 1
        if self._iter >= len(self):
            raise StopIteration
        return self.get_element(self._iter)

    def __len__(self) -> int:
        return self.element_count

    def __getitem__(self, index: int) -> Value:
        if not self:
            raise IndexError('Empty list.')
        while index < 0:
            index += len(self)
        while index >= len(self):
            index -= len(self)
        return self.get_element(index)

    @property
    def typing(self) -> Typing:
        return Typing(gsf.list_get_typing(self.handle))

    @property
    def size(self) -> int:
        return gsf.list_get_size[ct.c_size_t](self.handle)

    @size.setter
    def size(self, value: int) -> None:
        gsf.list_resize(self.handle, ct.c_size_t(value))

    @property
    def element_count(self) -> int:
        return gsf.list_element_count[ct.c_size_t](self.handle)

    def get_element(self, index: int) -> Value:
        return Value(gsf.list_get_element(self.handle, index), self.const)

    def add_element(self) -> Value:
        return Value(gsf.list_add_element(self.handle), False)

    @property
    def object(self) -> Iterable[Object]:
        return [v.decode_object() for v in self]

    @property
    def array(self) -> Iterable[Array]:
        return [v.decode_array() for v in self]

    @property
    def list(self) -> Iterable[List]:
        return [v.decode_list() for v in self]

    @property
    def map(self) -> Iterable[Map]:
        return [v.decode_map() for v in self]

    @property
    def i8(self) -> Iterable[int]:
        return [v.i8 for v in self]

    @property
    def i16(self) -> Iterable[int]:
        return [v.i16 for v in self]

    @property
    def i32(self) -> Iterable[int]:
        return [v.i32 for v in self]

    @property
    def i64(self) -> Iterable[int]:
        return [v.i64 for v in self]

    @property
    def u8(self) -> Iterable[int]:
        return [v.u8 for v in self]

    @property
    def u16(self) -> Iterable[int]:
        return [v.u16 for v in self]

    @property
    def u32(self) -> Iterable[int]:
        return [v.u32 for v in self]

    @property
    def u64(self) -> Iterable[int]:
        return [v.u64 for v in self]

    @property
    def f32(self) -> Iterable[int]:
        return [v.f32 for v in self]

    @property
    def f64(self) -> Iterable[int]:
        return [v.f64 for v in self]

    @property
    def string(self) -> Iterable[str]:
        return [v.string for v in self]


class Map:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const
        self._iter: int = -1

    @property
    def const(self) -> bool:
        return self._const

    def __bool__(self) -> bool:
        return len(self) > 0

    def __iter__(self) -> Map:
        self._iter = -1
        return self

    def __next__(self) -> tuple[str, Value]:
        self._iter += 1
        if self._iter >= len(self):
            raise StopIteration
        return self.get_key(self._iter), self.get_value(self._iter)

    def __len__(self) -> int:
        return self.element_count

    def __getitem__(self, index: int) -> tuple[str, Value]:
        if not self:
            raise IndexError('Empty map.')
        while index < 0:
            index += len(self)
        while index >= len(self):
            index -= len(self)
        return self.get_key(index), self.get_value(index)

    @property
    def typing(self) -> Typing:
        return Typing(gsf.map_get_typing(self.handle))

    @property
    def size(self) -> int:
        return gsf.map_get_size[ct.c_size_t](self.handle)

    @size.setter
    def size(self, value: int) -> None:
        gsf.map_resize(self.handle, ct.c_size_t(value))

    @property
    def element_count(self) -> int:
        return gsf.map_element_count[ct.c_size_t](self.handle)

    def get_key(self, index: int) -> str:
        return py_str(gsf.map_get_key[ct.c_char_p](self.handle, index))

    def get_value(self, index: int) -> Value:
        return Value(gsf.map_get_value(self.handle, index), self.const)

    def get(self, index: int) -> tuple[str, Value]:
        return (self.get_key(index), self.get_value(index))

    def contains(self, key: str) -> bool:
        return gsf.map_get_value_at_key[bool](self.handle, c_str(key))

    def value_at_key(self, key: str) -> Value:
        return Value(gsf.map_get_value_at_key(self.handle, c_str(key)), self.const)

    def add_element(self, key: str) -> Value:
        return Value(gsf.map_add_element(self.handle, c_str(key)), False)

    @property
    def object(self) -> Iterable[tuple[str, Object]]:
        return [(k, v.decode_object()) for (k, v) in self]

    @property
    def array(self) -> Iterable[tuple[str, Array]]:
        return [(k, v.decode_array()) for (k, v) in self]

    @property
    def list(self) -> Iterable[tuple[str, List]]:
        return [(k, v.decode_list()) for (k, v) in self]

    @property
    def map(self) -> Iterable[tuple[str, Map]]:
        return [(k, v.decode_map()) for (k, v) in self]

    @property
    def i8(self) -> Iterable[tuple[str, int]]:
        return [(k, v.i8) for (k, v) in self]

    @property
    def i16(self) -> Iterable[tuple[str, int]]:
        return [(k, v.i16) for (k, v) in self]

    @property
    def i32(self) -> Iterable[tuple[str, int]]:
        return [(k, v.i32) for (k, v) in self]

    @property
    def i64(self) -> Iterable[tuple[str, int]]:
        return [(k, v.i64) for (k, v) in self]

    @property
    def u8(self) -> Iterable[tuple[str, int]]:
        return [(k, v.u8) for (k, v) in self]

    @property
    def u16(self) -> Iterable[tuple[str, int]]:
        return [(k, v.u16) for (k, v) in self]

    @property
    def u32(self) -> Iterable[tuple[str, int]]:
        return [(k, v.u32) for (k, v) in self]

    @property
    def u64(self) -> Iterable[tuple[str, int]]:
        return [(k, v.u64) for (k, v) in self]

    @property
    def f32(self) -> Iterable[tuple[str, int]]:
        return [(k, v.f32) for (k, v) in self]

    @property
    def f64(self) -> Iterable[tuple[str, int]]:
        return [(k, v.f64) for (k, v) in self]

    @property
    def string(self) -> Iterable[tuple[str, str]]:
        return [(k, v.string) for (k, v) in self]


class Value:
    def __init__(self, handle, const: bool = True) -> None:
        self.handle = ct.c_void_p(handle)
        self._const = const

    @property
    def const(self) -> bool:
        return self._const

    @property
    def typing(self) -> Typing:
        return Typing(gsf.value_get_typing(self.handle))

    @property
    def type(self) -> Type:
        return Type(gsf.value_get_type(self.handle))

    def __bool__(self) -> bool:
        return self.is_set

    @property
    def is_set(self) -> bool:
        return gsf.value_get_type[bool](self.handle)

    def decode_object(self) -> Object:
        return Object(gsf.value_decode_object(self.handle), True)

    def encode_object(self, class_: Class | None) -> Object:
        return Object(gsf.value_encode_object(self.handle, class_.handle if class_ else None), False)

    def as_object(self, class_: Class | None) -> Object:
        return Object(gsf.value_as_object(self.handle, class_.handle if class_ else None), False)

    def decode_array(self) -> Array:
        return Array(gsf.value_decode_array(self.handle), True)

    def encode_array(self, type_: Type | str | None, size: int) -> Array:
        return Array(gsf.value_encode_array(
            self.handle, c_str_or(type_, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    def as_array(self, type_: Type | str | None, size: int) -> Array:
        return Array(gsf.value_as_array(
            self.handle, c_str_or(type_, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    def decode_list(self) -> List:
        return List(gsf.value_decode_list(self.handle), True)

    def encode_list(self, typing: Typing | str | None, size: int) -> List:
        return List(gsf.value_encode_list(
            self.handle, c_str_or(typing, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    def as_list(self, typing: Typing | str | None, size: int) -> List:
        return List(gsf.value_as_list(
            self.handle, c_str_or(typing, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    def decode_map(self) -> Map:
        return Map(gsf.value_decode_map(self.handle), True)

    def encode_map(self, typing: Typing | str | None, size: int) -> Map:
        return Map(gsf.value_encode_map(
            self.handle, c_str_or(typing, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    def as_map(self, typing: Typing | str | None, size: int) -> Map:
        return Map(gsf.value_as_map(
            self.handle, c_str_or(typing, lambda t: t.handle if t else None), ct.c_size_t(size)
        ), False)

    @property
    def i8(self) -> int:
        out = ct.c_int8()
        gsf.value_decode_i8[bool](self.handle, ct.pointer(out))
        return out.value

    @i8.setter
    def i8(self, value: int) -> None:
        gsf.value_encode_i8(self.handle, ct.c_int8(value))

    @property
    def i16(self) -> int:
        out = ct.c_int16()
        gsf.value_decode_i16[bool](self.handle, ct.pointer(out))
        return out.value

    @i16.setter
    def i16(self, value: int) -> None:
        gsf.value_encode_i16(self.handle, ct.c_int16(value))

    @property
    def i32(self) -> int:
        out = ct.c_int32()
        gsf.value_decode_i32[bool](self.handle, ct.pointer(out))
        return out.value

    @i32.setter
    def i32(self, value: int) -> None:
        gsf.value_encode_i32(self.handle, ct.c_int32(value))

    @property
    def i64(self) -> int:
        out = ct.c_int64()
        gsf.value_decode_i64[bool](self.handle, ct.pointer(out))
        return out.value

    @i64.setter
    def i64(self, value: int) -> None:
        gsf.value_encode_i64(self.handle, ct.c_int64(value))

    @property
    def u8(self) -> int:
        out = ct.c_uint8()
        gsf.value_decode_u8[bool](self.handle, ct.pointer(out))
        return out.value

    @u8.setter
    def u8(self, value: int) -> None:
        gsf.value_encode_u8(self.handle, ct.c_uint8(value))

    @property
    def u16(self) -> int:
        out = ct.c_uint16()
        gsf.value_decode_u16[bool](self.handle, ct.pointer(out))
        return out.value

    @u16.setter
    def u16(self, value: int) -> None:
        gsf.value_encode_u16(self.handle, ct.c_uint16(value))

    @property
    def u32(self) -> int:
        out = ct.c_uint32()
        gsf.value_decode_u32[bool](self.handle, ct.pointer(out))
        return out.value

    @u32.setter
    def u32(self, value: int) -> None:
        gsf.value_encode_u32(self.handle, ct.c_uint32(value))

    @property
    def u64(self) -> int:
        out = ct.c_uint64()
        gsf.value_decode_u64[bool](self.handle, ct.pointer(out))
        return out.value

    @u64.setter
    def u64(self, value: int) -> None:
        gsf.value_encode_u64(self.handle, ct.c_uint64(value))

    @property
    def f32(self) -> float:
        out = ct.c_float()
        gsf.value_decode_f32[bool](self.handle, ct.pointer(out))
        return out.value

    @f32.setter
    def f32(self, value: float) -> None:
        gsf.value_encode_f32(self.handle, ct.c_float(value))

    @property
    def f64(self) -> float:
        out = ct.c_double()
        gsf.value_decode_f64[bool](self.handle, ct.pointer(out))
        return out.value

    @f64.setter
    def f64(self, value: float) -> None:
        gsf.value_encode_f64(self.handle, ct.c_double(value))

    @property
    def string(self) -> str:
        return py_str(gsf.value_decode_str[ct.c_char_p](self.handle))

    @string.setter
    def string(self, value: str) -> None:
        gsf.value_encode_str(self.handle, c_str(value))
