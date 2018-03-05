#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2013 NotSqrt
#
# License: MIT
#

"""This module exports the Cppcheck plugin class."""

from SublimeLinter.lint import Linter, util


class Cppcheck(Linter):
    """Provides an interface to cppcheck."""

    syntax = ('c++', 'c', 'c improved')  # Able to handle C and C++ syntax
    cmd = ('cppcheck', '--template=gcc', '--inline-suppr', '--quiet', '*', '@')
    regex = (
        r'^(?P<file>.+):(?P<line>\d+):\s+'
        r'((?P<error>error)|(?P<warning>warning|style|performance|portability|information)):\s+'
        r'(?P<message>.+)'
    )
    error_stream = util.STREAM_BOTH  # linting errors are on stderr, exceptions like "file not found" on stdout
    tempfile_suffix = '-'
    defaults = {
        '--std=,+': [],  # example ['c99', 'c89']
        '--enable=,': 'style',
    }
    inline_settings = 'std'
    inline_overrides = 'enable'

    comment_re = r'\s*/[/*]'

    def split_match(self, match):
        """
        Return the components of the match.

        We override this because included header files can cause linter errors,
        and we only want errors from the linted file.

        """

        if match:
            if match.group('file') != self.filename:
                return None

        return super().split_match(match)
