import importlib
import unittest

import sublime
from SublimeLinter.lint.linter import VirtualView


Linters = importlib.import_module('SublimeLinter-cppcheck.linter')

# Captured cppcheck 2.21.0 output; accented characters and emoji count UTF-8 bytes.
SOURCE = (
    '#include <stdio.h>\n'
    'int main(void) {\n'
    '\tchar buf[4];\n'
    '\tprintf("é😀"); buf[10] = 0;\n'
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
    def test_captured_ascii_and_unicode_diagnostics_both_classes(self):
        lines = SOURCE.splitlines()
        expected = [(3, lines[3].index('[10]'), '['), (5, lines[5].index('p = 1'), 'p'),
                    (3, lines[3].index('= 0'), '='), (4, lines[4].index('= 5'), '=')]
        self.assertDiagnostics(OUTPUT, SOURCE, expected)

    def test_raw_byte_columns_exceed_line_length_both_classes(self):
        source = '\tprintf("é😀😀😀😀"); buf[10] = 0;'
        for column, text in [(35, '['), (40, '=')]:
            with self.subTest(column=column):
                output = 'm.c:1:{}:error:rule:problem'.format(column)
                self.assertDiagnostics(output, source, [(0, source.index(text), text)])

    def assertDiagnostics(self, output, source, expected):
        for cls in (Linters.Cppcheck, Linters.CppcheckPlus):
            with self.subTest(linter=cls.name):
                linter = cls(sublime.View(0), {})
                vv = VirtualView(source)
                matches = list(linter.find_errors(output))
                self.assertEqual(len(matches), len(expected))
                for match, (line, col, text) in zip(matches, expected):
                    match['filename'] = None
                    error = linter.process_match(match, vv)
                    self.assertIsNotNone(error)
                    begin = vv.full_line(line)[0] + col
                    self.assertEqual({k: error[k] for k in ('line', 'start', 'region', 'offending_text')}, {
                        'line': line, 'start': col, 'region': sublime.Region(begin, begin + len(text)),
                        'offending_text': text,
                    })
