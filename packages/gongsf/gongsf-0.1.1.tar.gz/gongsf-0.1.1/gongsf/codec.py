import ctypes as ct
from .lib import gsf, c_str, py_str
from .data import Descriptor, Schema, Article

def _parse_flags(prefix: str, flags: dict[str, bool]) -> ct.c_int:
    field = 0
    for flag, val in flags.items():
        if not val:
            continue
        field |= int(gsf.macros("gsf_codec.h")[prefix + '_' + flag], 2)
    return ct.c_int(field)

# this represets both gsf_reader and gsf_writer
class GsfCodecStruct(ct.Structure):
    _fields_ = [
        ('format', ct.c_int),
        ('flags', ct.c_int),
        ('_datas', ct.c_byte * 32),
    ]

def read_schema_txt(
        string: str, *,
        save_comments=False, no_comments=False,
) -> tuple[Descriptor, Schema]:
    descriptor = Descriptor(gsf.create_descriptor(), own=True)
    schema = Schema(gsf.create_schema(), own=True, descriptor=descriptor)
    reader = GsfCodecStruct()
    reader.format = 0
    reader.flags = _parse_flags('TXT_READ', {
        'SAVE_COMMENTS': save_comments,
        'NO_COMMENTS': no_comments,
    })
    cstr = c_str(string)
    gsf.reader_create_buf(ct.pointer(reader), cstr, ct.c_size_t(len(string) + 1))
    gsf.read_schema(ct.pointer(reader), schema.handle, descriptor.handle)
    gsf.reader_delete_buf(ct.pointer(reader))
    return descriptor, schema


def read_article_txt(
        string: str, schema: Schema, *,
        save_comments=False, no_comments=False,
) -> Article:
    article = Article(gsf.create_article(), own=True)
    reader = GsfCodecStruct()
    reader.format = 0
    reader.flags = _parse_flags('TXT_READ', {
        'SAVE_COMMENTS': save_comments,
        'NO_COMMENTS': no_comments,
    })
    cstr = c_str(string)
    gsf.reader_create_buf(ct.pointer(reader), cstr, ct.c_size_t(len(cstr) + 1))
    gsf.read_article(ct.pointer(reader), article.handle, schema.handle)
    gsf.reader_delete_buf(ct.pointer(reader))
    return article


def write_schema_txt(
        schema: Schema, max_size: int = 2048, *,
        signature=False, comments=False, no_header_newline=False,
        no_label_doc=False,
) -> str:
    writer = GsfCodecStruct()
    writer.format = 0
    writer.flags = _parse_flags('TXT_WRITE', {
        'SIGNATURE': signature,
        'COMMENTS': comments,
        'NO_HEADER_NEWLINE': no_header_newline,
        'SCHEMA_NO_LABEL_DOC': no_label_doc,
    })
    string = ct.create_string_buffer(max_size)
    gsf.writer_create_buf(ct.pointer(writer), string, ct.c_size_t(max_size))
    gsf.write_article(ct.pointer(writer), schema.handle)
    gsf.writer_delete_buf(ct.pointer(writer))
    return py_str(string.value)


def write_article_txt(
        article: Article, max_size_deprecated: int = 0, *,
        signature=False, comments=False, no_header_newline=False,
        no_descriptor=False, strong_all=False, strong_root=False, strong_types=False,
) -> str:
    writer = GsfCodecStruct()
    writer.format = 0
    writer.flags = _parse_flags('TXT_WRITE', {
        'SIGNATURE': signature,
        'COMMENTS': comments,
        'NO_HEADER_NEWLINE': no_header_newline,
        'ARTICLE_NO_DESCRIPTOR': no_descriptor,
        'ARTICLE_STRONG_TYPES_ALL': strong_all,
        'ARTICLE_STRING_ROOT': strong_root,
        'ARTICLE_STRING_TYPES': strong_types,
        'LEADING_ZERO': True,
    })
    buf = ct.c_char_p()
    gsf.writer_create_growing_buf(ct.pointer(writer), ct.pointer(buf), ct.c_size_t(0))
    gsf.write_article(ct.pointer(writer), article.handle)
    result = py_str(buf.value)
    gsf.writer_delete_growing_buf(ct.pointer(writer))
    return result
