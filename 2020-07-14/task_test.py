import unittest

from task import order
class OrderTest(unittest.TestCase):

    def test_1(self):
        result = order('begi4n th2e Le1t 3game')
        self.assertEqual(result, 'Le1t th2e 3game begi4n')

    def test_2(self):
        result = order('чт2о попр4обовать э6то 5написать де7ло 1А кириллице8й? если3')
        self.assertEqual(result, '1А чт2о если3 попр4обовать 5написать э6то де7ло кириллице8й?')

    def test_3(self):
        result = order('3BATMAN все5 8а ч9е к7учу nanan1ana BATMA2N сме4шаем 6в')
        self.assertEqual(result, 'nanan1ana BATMA2N 3BATMAN сме4шаем все5 6в к7учу 8а ч9е')

    def test_4(self):
        result = order('wrong4 wi5th w2hat i6t Che1ck we3nt')
        self.assertEqual(result, 'Che1ck w2hat we3nt wrong4 wi5th i6t')



if __name__ == '__main__':
    unittest.main()