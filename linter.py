from SublimeLinter.lint import Linter, util


class Cppcheck(Linter):
    cmd = (
        'cppcheck',
        '--template={file}:{line}:{column}:{severity}:{id}:{message}',
        '--inline-suppr',
        '--quiet',
        '${args}',
        '${file}'
    )
    regex = (
        r'^(?P<filename>(:\\|[^:])+):(?P<line>\d+):((?P<col>\d+):)'
        r'((?P<error>error)|(?P<warning>warning|style|performance|portability|information)):'
        r'(?P<code>\w+):(?P<message>.+)'
    )
    error_stream = util.STREAM_BOTH  # linting errors are on stderr, exceptions like "file not found" on stdout
    on_stderr = None  # handle stderr via split_match
    tempfile_suffix = '-'
    defaults = {
        'selector': 'source.c, source.c++',
        '--std=,+': [],  # example ['c99', 'c89']
        '--enable=,': 'style',
    }
