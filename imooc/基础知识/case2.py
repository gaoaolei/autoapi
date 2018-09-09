import unittest
def div(x, y):
    return x*y
class Case2(unittest.TestCase):
    def testDiv(self):
        print('dddddddddd')
    def tearDown(self):
        print('dddddddddddddddddddddddd')