import unittest

from solution import palindrome_permutation


class TestPalindromePermutation(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))
        self.assertTrue(palindrome_permutation(""))
        self.assertTrue(palindrome_permutation("a"))
        self.assertTrue(palindrome_permutation("aa"))
        self.assertTrue(palindrome_permutation("aaa"))
        self.assertTrue(palindrome_permutation("aab"))
        self.assertTrue(palindrome_permutation("aba"))
        self.assertFalse(palindrome_permutation("ab"))
        self.assertFalse(palindrome_permutation("abc"))
        self.assertFalse(palindrome_permutation("abbc"))
        self.assertFalse(palindrome_permutation("abcc"))
        self.assertFalse(palindrome_permutation("abccc"))
        self.assertFalse(palindrome_permutation("abcccc"))


if __name__ == "__main__":
    unittest.main()
