import unittest

from solution import URLify


class TestURLify(unittest.TestCase):
    def test_URLify(self):
        self.assertEqual(URLify("Mr John Smith    ", 13), "Mr%20John%20Smith")


if __name__ == "__main__":
    unittest.main()
