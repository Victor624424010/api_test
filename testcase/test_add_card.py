import requests
import unittest
import json
from conf import config
from lib.db import chack_card,del_card
from lib.load_data import get_case,get_sheet
from lib.case_log import log_case_info

class TestAddCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):#整个测试类的测试准备方法
        cls.sheet=get_sheet(config.data_file,'添加卡')#公用方法
    # @unittest.skipUnless(db.chack_card('621660041112756'),'跳过该测试用例')
    def test_add_normal(self):
        case_data=get_case(self.sheet,'test_add_normal')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url,json=data)
        # print(type(excepted_res))
        print(res.json())
        log_case_info('test_add_normal',url,case_data[3],case_data[4],res.json())
        self.assertDictEqual(excepted_res,res.json())#字典相等
        # self.assertEqual(res.json()['msg'],'添加卡成功')
        # self.assertIs(res.json()['code'],200)
        self.assertTrue(chack_card('621660041112756'))

        del_card('621660041112756')

    def test_add_wrong(self):
        case_data = get_case(self.sheet, 'test_add_wrong')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        log_case_info('test_add_wrong',url,case_data[3],case_data[4],res.json())
        print(res.json())
        self.assertDictEqual(excepted_res,res.json())
        # self.assertEqual(res.json()['msg'], '该卡已添加')
        # self.assertEqual(res.json()['code'],5000)


if __name__ == '__main__':
    unittest.main(verbosity=2)

