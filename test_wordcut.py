import unittest

from wordcut import wrap


class WordcutTest(unittest.TestCase):
    def test_wrap(self) -> None:
        self.assertEqual(wrap("one two three", 7), ["one two", "three"])
        self.assertEqual(wrap("", 4), [])


if __name__ == "__main__":
    unittest.main()
