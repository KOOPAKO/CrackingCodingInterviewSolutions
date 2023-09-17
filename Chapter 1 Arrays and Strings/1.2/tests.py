import unittest

from solution import check_permutation


class Test_is_permutation(unittest.TestCase):
    """
    Class for testing is_permutation.
    """

    def test_is_permutation(self):
        """
        Tests is_permutation on two strings that are permutations.
        """
        self.assertTrue(check_permutation("abcd", "dcba"))

    def test_is_not_permutation(self):
        """
        Tests is_permutation on two strings that are not permutations.
        """
        self.assertFalse(check_permutation("abcd", "abca"))

    def test_is_not_permutation_different_lengths(self):
        """
        Tests is_permutation on two strings that are not permutations because
        they are different lengths.
        """
        self.assertFalse(check_permutation("abcd", "abc"))

    def test_empty_string(self):
        """
        Tests is_permutation on an empty string.
        """
        self.assertTrue(check_permutation("", ""))


if __name__ == "__main__":
    unittest.main()
