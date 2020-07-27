import unittest
from ticktacktoe import is_solved

class TickTackToeTest(unittest.TestCase):

    def test_1(self):
        result = is_solved([[1,0,2], [1,0,0], [1,2,2]])
        self.assertEqual(result, 1)

    def test_2(self):
        result = is_solved([[1,2,1], [2,2,2], [2,1,2]])
        self.assertEqual(result, 2)

    def test_3(self):
        result = is_solved([[0,1,0], [0,2,1], [0,1,0]])
        self.assertEqual(result, -1)

    def test_4(self):
        result = is_solved([[2,1,2],[2,1,1],[1,2,1]])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
