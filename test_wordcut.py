import unittest

from wordcut import line_count, longest_line, wrap, wrap_text


class WordcutTest(unittest.TestCase):
    def test_wrap(self) -> None:
        self.assertEqual(wrap("one two three", 7), ["one two", "three"])
        self.assertEqual(wrap("", 4), [])
        self.assertEqual(wrap_text("one two three", 7), "one two\nthree")
        self.assertEqual(line_count("one two three", 7), 2)
        self.assertEqual(line_count("", 4), 0)
        self.assertEqual(longest_line("one two three", 7), 7)
        self.assertEqual(longest_line("", 4), 0)


if __name__ == "__main__":
    unittest.main()
