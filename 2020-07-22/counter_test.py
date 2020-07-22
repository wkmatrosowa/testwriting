import unittest
from counter import count

class CounterTest(unittest.TestCase):

    def test_1(self):
        result = count('')
        self.assertEqual(result, {})

    def test_2(self):
        result = count('MyHeartWillGoOn')
        self.assertEqual(result, {'M': 1, 'y': 1, 'H': 1, 'e': 1, 'a': 1, 'r': 1, 't': 1, 'W': 1, 'i': 1, 'l': 2, 'G': 1, 'o': 1, 'O': 1, 'n': 1})

    def test_3(self):
        result = count('HAHAHAHAHAHAHA')
        self.assertEqual(result, {'H': 7, 'A': 7})

    def test_4(self):
        result = count('12341234')
        self.assertEqual(result, {'1': 2, '2': 2, '3': 2, '4': 2})


if __name__ == '__main__':
    unittest.main()
