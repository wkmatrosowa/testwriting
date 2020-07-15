import unittest
from find_missing_letter import find_missing_letter

class FindMissingLetterTest(unittest.TestCase):
    def test_1(self):
        result = find_missing_letter(['C', 'E', 'F'])
        self.assertEqual(result, 'D')

    def test_2(self):
        result = find_missing_letter(['u', 'v', 'w', 'y', 'z'])
        self.assertEqual(result, 'x')

    def test_3(self):
        result = find_missing_letter(['j', 'l', 'm', 'n'])
        self.assertEqual(result, 'k')

    def test_4(self):
        result = find_missing_letter(['N', 'O', 'P', 'R'])
        self.assertEqual(result, 'Q')


if __name__ == '__main__':
    unittest.main()
