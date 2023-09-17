import unittest

from solution import is_unique


class Test_is_unique(unittest.TestCase):
    """
    Class for testing is_unique.
    """

    def test_is_unique(self):
        """
        Tests is_unique on a string with unique characters.
        """
        self.assertTrue(is_unique("abcd"))

    def test_is_not_unique(self):
        """
        Tests is_unique on a string with non-unique characters.
        """
        self.assertFalse(is_unique("abca"))

    def test_empty_string(self):
        """
        Tests is_unique on an empty string.
        """
        self.assertTrue(is_unique(""))


if __name__ == "__main__":
    unittest.main()
