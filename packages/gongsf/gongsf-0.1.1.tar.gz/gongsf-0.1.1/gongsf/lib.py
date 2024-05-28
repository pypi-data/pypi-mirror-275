from __future__ import annotations
from platform import system as system_name
from os import environ
from pathlib import Path
import ctypes as ct
import re
from typing import Any, Callable

# TODO const check before mutable methods


class GsfException(Exception):
    pass

def gsf_raise() -> None:
    error = ct.create_string_buffer(2048)
    gsf.errno_string(error, no_except=True)
    err = py_str(error.value)
    if err == 'no error':
        return
    raise GsfException(err)


class GsfSymbol:
    def __init__(self, symbol, name: str):
        symbol.restype = ct.c_void_p
        self._symbol = symbol
        self._bool = False
        self._name = name

    def __call__(self, *args, **kwargs) -> Any:
        error_val = kwargs.get('error', None)
        no_except = kwargs.get('no_except', False) or self._symbol.restype is None
        ret = self._symbol(*args, **kwargs)
        if self._bool:
            return ret is not None
        if not no_except and ret == error_val:
            gsf_raise()
            return ret
        return ret

    def __getitem__(self, item: type | None) -> GsfSymbol:
        if item != ct.c_bool:
            self._symbol.restype = item
        else:
            self._bool = True
        return self


class GsfMacros:
    def __init__(self, header: Path) -> None:
        self.macros: dict[str, str] = {}
        if not header.exists():
            return
        string = header.read_text('utf-8')
        matches = re.findall(r'#define[ \t]+GSF_([A-Z_]+)[ \t]+([^/\n]+)', string)
        for name, replacement in matches:
            self.macros[name] = replacement

    def __getitem__(self, name: str) -> str:
        return self.macros[name]


class GsfLib(ct.CDLL):
    def __init__(self, lib_name: Path, header_dir: Path) -> None:
        super().__init__(str(lib_name))
        self.header_dir = header_dir
        self._macros: dict[str, GsfMacros] = {}

    def __getattr__(self, name: str) -> GsfSymbol:
        prefix = 'gsf_'
        if name[0].isupper():
            prefix = prefix.upper()
        return GsfSymbol(super().__getattr__(prefix + name), prefix + name)

    def macros(self, header: str) -> GsfMacros:
        if header not in self._macros:
            self._macros[header] = GsfMacros(self.header_dir / header)
        return self._macros[header]


lib_path: Path | str | None = None
KNOWN_PATHS_LINUX_LIB = [
    "/lib/libgsf.so.0.1",
    "/usr/lib/libgsf.so.0.1",
    "/usr/local/lib/libgsf.so.0.1",
    "/lib/libgsf.so",
    "/usr/lib/libgsf.so",
    "/usr/local/lib/libgsf.so",
]
if 'GSF_LIB' in environ:
    lib_path = environ['GSF_LIB']
elif system_name() == 'Linux':
    for lib_path in KNOWN_PATHS_LINUX_LIB:
        if Path(lib_path).exists():
            break
    else:
        lib_path = None
include_path: Path | str | None = None
KNOWN_PATHS_LINUX_INCLUDE = [
    "/include/gongsf",
    "/usr/include/gongsf",
    "/usr/local/include/gongsf",
]
if 'GSF_INCLUDE' in environ:
    include_path = environ['GSF_INCLUDE']
elif system_name() == 'Linux':
    for include_path in KNOWN_PATHS_LINUX_INCLUDE:
        if Path(include_path).exists():
            break
    else:
        include_path = None

if lib_path is None:
    raise RuntimeError('Could not deduce GSF library location. Please, install GSF Lib and/or set define $GSF_LIB.')
if include_path is None:
    raise RuntimeError('Could not deduce GSF header directory. Please, install GSF Lib and/or set define $GSF_INCLUDE.')
gsf = GsfLib(Path(lib_path), Path(include_path))


def c_str_or(py: str | Any, callback: Callable[[Any], Any]):
    if isinstance(py, str):
        return py.encode('utf-8')
    else:
        return callback(py)


def c_str(py: str | Any):
    return c_str_or(py, lambda x: x)


def py_str(c):
    return c.decode('utf-8')
