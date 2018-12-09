import unittest
from testcase import test_add_card

suite = unittest.TestSuite()
suite.addTest()



#遍历所有用例
suite = unittest.defaultTestLoader.discover('.')
#添加模块所有用例
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_add_card)

#添加类中所有测试用例
loader.loadTestsFromTestCase()


#按名称添加
loader.loadTestsFromName('')
