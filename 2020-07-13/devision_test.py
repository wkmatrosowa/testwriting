import unittest

def devision(a, b):
    return a / b if b != 0 else 'It is impossible to do that'

class DevisionTest(unittest.TestCase):
    def test_1(self):
        result = devision(4, 4)
        self.assertEqual(result, 1)

    def test_2(self):
        result = devision(-1, 4)
        self.assertEqual(result, -0.25)

    def test_3(self):
        result = devision(10, 0)
        self.assertEqual(result, 'It is impossible to do that')


if __name__ == '__main__':
    unittest.main()
