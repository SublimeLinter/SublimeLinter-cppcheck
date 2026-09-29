from SublimeLinter.lint import Linter, util

CMD = (
    "cppcheck",
    "--template={file}:{line}:{column}:{severity}:{id}:{message}",
    "--inline-suppr",
    "--quiet",
    "${args}",
    "${file}",
)

REGEX = (
    r"^(?P<filename>(:\\|[^:])+):(?P<line>\d+):((?P<col>\d+):)"
    r"((?P<error>error)|(?P<warning>warning|style|performance|portability|information)):"
    r"(?P<code>\w+):(?P<message>.+)"
)


def byte_offset_to_index(text, offset):
    """Return the index in `text` of the character at UTF-8 byte `offset`."""
    return len(text.encode('utf-8')[:offset].decode('utf-8', 'ignore'))


class CppcheckBase(Linter):
    __abstract__ = True

    def reposition_match(self, line, col, m, vv):
        if col is not None:
            # cppcheck reports the column as a byte offset into the UTF-8 line,
            # so every non-ASCII character before the error shifts it. Sublime
            # counts characters.
            col = byte_offset_to_index(vv.select_line(line), col)

        return super().reposition_match(line, col, m, vv)


class Cppcheck(CppcheckBase):
    cmd = CMD
    regex = REGEX
    error_stream = util.STREAM_BOTH  # linting errors are on stderr, exceptions like "file not found" on stdout
    on_stderr = None  # handle stderr via split_match
    tempfile_suffix = "-"

    defaults = {
        "selector": "source.c",
        "--language=": "c",
        "--std=,+": [],  # example ['c89', 'c99', 'c11']
        "--enable=,": "style",
    }


class CppcheckPlus(CppcheckBase):
    cmd = CMD
    regex = REGEX
    error_stream = util.STREAM_BOTH  # linting errors are on stderr, exceptions like "file not found" on stdout
    on_stderr = None  # handle stderr via split_match
    tempfile_suffix = "-"

    name = 'cppcheck++'
    defaults = {
        "selector": "source.c++",
        "--language=": "c++",
        "--std=,+": [],  # example ['c++03', 'c++11', 'c++14', 'c++17', 'c++20']
        "--enable=,": "style",
    }
