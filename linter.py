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


class CppcheckC(Linter):
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


class CppcheckCpp(Linter):
    cmd = CMD
    regex = REGEX
    error_stream = util.STREAM_BOTH  # linting errors are on stderr, exceptions like "file not found" on stdout
    on_stderr = None  # handle stderr via split_match
    tempfile_suffix = "-"

    defaults = {
        "selector": "source.c++",
        "--language=": "c++",
        "--std=,+": [],  # example ['c++03', 'c++11', 'c++14', 'c++17', 'c++20']
        "--enable=,": "style",
    }
