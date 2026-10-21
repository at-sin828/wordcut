import unittest

from wordcut import fits, line_count, longest_line, longest_word, one_line, overlong, shortest_line, word_count, wrap, wrap_text


class WordcutTest(unittest.TestCase):
    def test_wrap(self) -> None:
        self.assertEqual(wrap("one two three", 7), ["one two", "three"])
        self.assertEqual(wrap("", 4), [])
        self.assertEqual(wrap_text("one two three", 7), "one two\nthree")
        self.assertEqual(line_count("one two three", 7), 2)
        self.assertEqual(line_count("", 4), 0)
        self.assertEqual(longest_line("one two three", 7), 7)
        self.assertEqual(longest_line("", 4), 0)
        self.assertEqual(shortest_line("one two three", 7), 5)
        self.assertEqual(shortest_line("", 4), 0)
        self.assertFalse(one_line("one two three", 7))
        self.assertTrue(one_line("one", 7))
        self.assertEqual(overlong("one two three", 4), ["three"])
        self.assertEqual(word_count("one two three"), 3)
        self.assertEqual(word_count(""), 0)
        self.assertTrue(fits("one two", 4))
        self.assertFalse(fits("one two three", 4))
        self.assertEqual(longest_word("one two three"), 5)
        self.assertEqual(longest_word(""), 0)


if __name__ == "__main__":
    unittest.main()
