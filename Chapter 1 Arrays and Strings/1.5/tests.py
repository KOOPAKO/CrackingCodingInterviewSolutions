import unittest

from solution import one_away


class TestOneAway(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away("", ""))
        self.assertTrue(one_away("", "a"))
        self.assertTrue(one_away("a", ""))
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertTrue(one_away("ples", "pales"))
        self.assertTrue(one_away("pale", "pkle"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pale", "pse"))
        self.assertFalse(one_away("pale", "pas"))
        self.assertFalse(one_away("pas", "pale"))
        self.assertFalse(one_away("pkle", "pable"))
        self.assertFalse(one_away("pal", "palks"))


if __name__ == "__main__":
    unittest.main()
