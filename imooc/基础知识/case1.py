import unittest
from 6 import RunMethod
def multi(x, y):
    return x*y
class Case1(unittest.TestCase):
    def testMulti(self):
        print('hhhhhh')
        url = 'https://xiaoshuo.km.com/api/v1/bookshelf-adv?gender=2&sign=630fb29dde5d9084cc3c11647bc093d4'
        RunMethod()
    def setUp(self):
        print('setuphhahahha')