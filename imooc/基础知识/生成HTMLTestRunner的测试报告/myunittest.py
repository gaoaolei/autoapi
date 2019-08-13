import unittest
from HTMLTestRunner import HTMLTestRunner
def add(x, y):
    return x+y
'单元测试'
class RunCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass')
    # @unittest.skip('True')
    def test_00001(self):
        # self.skipTest('ajds')
        print('001case')
        self.assertEqual(add(1, 2), 4)
    def test_002(self):
        print('002test')
    def test_004(self):
        print('003caseeeeeeeeeeeeeeeeeeee33333e')
        self.assertEqual(add(1, 2), 3)
    def setUp(self):
        print('setup')
    def tearDown(self):
        print('teardown')
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['myunittest.RunCase']))
    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='test report from gaoaolei',
                                description='prepare for interface test',
                                verbosity=2)# 这里面包含写内容了
        print('write successful!')
        runner.run(suite)
