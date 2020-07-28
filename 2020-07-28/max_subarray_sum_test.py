import unittest
from max_subarray_sum import max_subarray_sum


class MaxSubarrayTest(unittest.TestCase):

    def test_1(self):
        result = max_subarray_sum([])
        self.assertEqual(result, 0)

    def test_2(self):
        result = max_subarray_sum([-3, -45555, -63, -52, -67, -76, -7, -4, -43])
        self.assertEqual(result, 0)

    def test_3(self):
        result = max_subarray_sum([-3, -45555, -63, -52, -67, 76, -7, -4, -43])
        self.assertEqual(result, 76)

    def test_4(self):
        result = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
