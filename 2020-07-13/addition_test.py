import unittest

def addition(a, b):
    return a + b

class AdditionTest(unittest.TestCase):
    def test_1(self):
        result = addition(3, 4)
        self.assertEqual(result, 7)

    def test_2(self):
        result = addition(-1, 4)
        self.assertEqual(result, 3)

    def test_3(self):
        result = addition(-4, 1)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()