import unittest

def multiplication(a, b):
    return a * b

class MultiplicationTest(unittest.TestCase):
    def test_1(self):
        result = multiplication(4, 4)
        self.assertEqual(result, 16)

    def test_2(self):
        result = multiplication(-1, 0)
        self.assertEqual(result, 0)

    def test_3(self):
        result = multiplication(10, 15)
        self.assertEqual(result, 150)


if __name__ == '__main__':
    unittest.main()
