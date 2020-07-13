import unittest

def subtraction(a, b):
    return a - b

class SubtractionTest(unittest.TestCase):

    def test_1(self):
        result = subtraction(5, 4)
        self.assertEqual(result, 1)

    def test_2(self):
        result = subtraction(-5, -10)
        self.assertEqual(result, 5)

    def test_3(self):
        result = subtraction(10, 15)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()
