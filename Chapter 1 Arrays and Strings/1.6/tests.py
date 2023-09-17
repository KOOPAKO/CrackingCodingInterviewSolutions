import unittest

from solution import string_compression


class TestStringCompression(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("abcdef"), "abcdef")
        self.assertEqual(string_compression("aaaabbbccd"), "a4b3c2d1")
        self.assertEqual(string_compression(""), "")


if __name__ == "__main__":
    unittest.main()
