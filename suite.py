import unittest
from testcase.test_add_card import TestAddCard
from testcase.test_tied_card import TestTiedCard
from testcase import test_add_card


#遍历所有用例
suite = unittest.defaultTestLoader.discover('./testcase')


smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestAddCard('test_add_normal'),
                     TestAddCard('test_add_wrong')])
smoke_suite.addTest(TestAddCard('test_add_wrong'))
smoke_suite.addTests([TestTiedCard('test_tied_card_normal'),
                     TestTiedCard('test_tied_card_wrong')])
smoke_suite.addTest(TestTiedCard('test_tied_card_wrong'))


#添加模块所有用例
# loader = unittest.TestLoader()
# suite = loader.loadTestsFromModule(test_add_card)

#添加类中所有测试用例
# loader.loadTestsFromTestCase()

#按名称添加
# loader.loadTestsFromName('')

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)