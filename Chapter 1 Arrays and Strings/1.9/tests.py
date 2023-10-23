import unittest

from solution import is_rotation

class Test(unittest.TestCase):
    def test1(self):
        string = "waterbottle"
        candidate = "erbottlewat"
        self.assertEqual(is_rotation(string, candidate), True)

    def test2(self):
        string = "waterbottle"
        candidate = "erbottlewa"
        self.assertEqual(is_rotation(string, candidate), False)

    def test3(self):
        string = "waterbottle"
        candidate = "waterbottle"
        self.assertEqual(is_rotation(string, candidate), True)   

    def test4(self):
        string = "supercalifragilisticexpialidocious"
        candidate = "cexpialidocioussupercalifragilisti"
        self.assertEqual(is_rotation(string, candidate), True)

    def test5(self):
        string = "supercalifragilisticexpialidocious"
        candidate = "cexpialidocioussupercalifragilist"
        self.assertEqual(is_rotation(string, candidate), False)


if __name__ == "__main__":
    unittest.main()