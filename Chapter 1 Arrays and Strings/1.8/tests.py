import unittest

from solution import zero_matrix


class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        expected = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
        self.assertEqual(zero_matrix(matrix), expected)

        matrix = [[1, 2, 3, 4], [5, 6, 0, 8],
                  [9, 10, 11, 12], [13, 0, 15, 16]]
        expected = [[1, 0, 0, 4], [0, 0, 0, 0],
                    [9, 0, 0, 12], [0, 0, 0, 0]]
        self.assertEqual(zero_matrix(matrix), expected)

        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0],
                  [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        expected = [[1, 2, 3, 4, 0], [0, 0, 0, 0, 0],
                    [11, 12, 13, 14, 0], [16, 17, 18, 19, 0],
                    [21, 22, 23, 24, 0]]
        self.assertEqual(zero_matrix(matrix), expected)

        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(zero_matrix(matrix), matrix)


if __name__ == "__main__":
    unittest.main()
    