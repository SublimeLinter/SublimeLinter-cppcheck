import importlib
import unittest

import sublime
from SublimeLinter.lint.linter import VirtualView


LinterModule = importlib.import_module('SublimeLinter-cppcheck.linter')


# Real output of `cppcheck --template={file}:{line}:{column}:{severity}:{id}:{message}
# --inline-suppr --quiet --enable=style --language=c m.c` (cppcheck 2.21.0) for this source.
# cppcheck counts the column in bytes of the UTF-8 line: the 'e' with acute accent is two
# bytes and the emoji (U+1F600) four.
SOURCE = (
    '#include <stdio.h>\n'
    'int main(void) {\n'
    '\tchar buf[4];\n'
    '\tprintf("é\U0001f600"); buf[10] = 0;\n'
    '\tint x = 5;\n'
    '\tint *p = 0; *p = 1;\n'
    '\treturn 0;\n'
    '}\n'
)
OUTPUT = (
    "m.c:4:23:error:arrayIndexOutOfBounds:Array 'buf[4]' accessed at index 10, which is out of bounds.\n"
    "m.c:6:15:error:nullPointer:Null pointer dereference: p\n"
    "m.c:4:28:style:unreadVariable:Variable 'buf[10]' is assigned a value that is never used.\n"
    "m.c:5:8:style:unreadVariable:Variable 'x' is assigned a value that is never used.\n"
)


class TestColumns(unittest.TestCase):
    def resolve(self, linter_class):
        linter = linter_class(sublime.View(0), {})
        vv = VirtualView(SOURCE)
        return [
            (m['line'], linter.reposition_match(m['line'], m['col'], m, vv)[1])
            for m in linter.find_errors(OUTPUT)
        ]

    def expected(self):
        lines = SOURCE.split('\n')
        return [
            (3, lines[3].index('[10]')),        # `buf[10]`: cppcheck points at the `[`
            (5, lines[5].index('p = 1')),       # the dereferenced `p`
            (3, lines[3].index('= 0')),         # the assignment of `buf[10]`
            (4, lines[4].index('= 5')),         # `int x = 5`
        ]

    def test_columns_after_non_ascii_characters_are_characters(self):
        for linter_class in (LinterModule.Cppcheck, LinterModule.CppcheckPlus):
            self.assertEqual(self.resolve(linter_class), self.expected())

    def test_ascii_line_is_unchanged(self):
        f = LinterModule.byte_offset_to_index
        self.assertEqual(f('\tint x = 5;', 7), 7)
        self.assertEqual(f('abc', 0), 0)

    def test_multibyte_characters_count_their_bytes(self):
        f = LinterModule.byte_offset_to_index
        text = 'é\U0001f600x'        # 2 + 4 + 1 bytes
        self.assertEqual(f(text, 2), 1)    # after the first character
        self.assertEqual(f(text, 6), 2)    # `x`
        self.assertEqual(f(text, 7), 3)    # end of line

    def test_offset_inside_a_character_or_past_the_end_does_not_fail(self):
        f = LinterModule.byte_offset_to_index
        self.assertEqual(f('\U0001f600x', 2), 0)
        self.assertEqual(f('ab', 9), 2)
