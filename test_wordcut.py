import unittest

from wordcut import wrap, wrap_text


class WordcutTest(unittest.TestCase):
    def test_wrap(self) -> None:
        self.assertEqual(wrap("one two three", 7), ["one two", "three"])
        self.assertEqual(wrap("", 4), [])
        self.assertEqual(wrap_text("one two three", 7), "one two\nthree")


if __name__ == "__main__":
    unittest.main()
