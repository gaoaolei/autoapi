import unittest
# import case1
# # from case1 import Case1
# from case2 import Case2
# # import case1
from HTMLTestRunner import HTMLTestRunner
def add(x, y):
    return x+y
'单元测试'
class RunCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass')
    # @unittest.skip('True')
    def test_001(self):
        # self.skipTest('ajds')
        print('001case')
        self.assertEqual(add(1, 2), 4)
    def test_002(self):
        print('002test')
    def test_003(self):
        print('003case')
        self.assertEqual(add(1, 2), 3)
    def setUp(self):
        print('setup')
    def tearDown(self):
        print('teardown')
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

if __name__ == "__main__":
    # unittest.main() #main()实质是调用TextTestRunner()中的run()函数，所以=unittest.TextTestRunner().run()
    # unittest.TextTestRunner().run()
    suite = unittest.TestSuite()
    # print(suite)
    # suite.addTest(RunCase('test_003'))
    # print(suite)
    # unittest.TextTestRunner().run(suite)
    # loadTestFromName方法不需要导入模块
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['myunittest.RunCase', 'case2.Case2', 'case1.Case1']))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(case1.Case1))
    # unittest.TextTestRunner().run(suite)
    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='test report from gaoaolei',
                                description='prepare for interface test',
                                verbosity=2)
        runner.run(suite)