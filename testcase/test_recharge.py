import unittest
import requests
import json
from conf import config
from lib import load_data
from lib.case_log import log_case_info

class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,'充值')
    def test_recharge_normal(self):
        case_data = load_data.get_case(self.sheet,'test_recharge_normal')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url,json=data)
        print(res.json())
        log_case_info('test_recharge_normal',case_data[2],case_data[3],case_data[4],res.json())
        # self.assertDictEqual(excepted_res,res.json())
        self.assertEqual(res.json()['msg'],'充值成功')
        self.assertEqual(res.json()['code'],200)

    def test_recharge_wrong(self):
        case_data = load_data.get_case(self.sheet,'test_recharge_wrong')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url,json=data)
        print(res.json())
        log_case_info('test_recharge_wrong',case_data[2],case_data[3],case_data[4],res.json())
        self.assertDictEqual(excepted_res,res.json())
        # self.assertEqual(res.json()['msg'],'金额需为整数')
        # self.assertEqual(res.json()['code'], 300)
if __name__ == '__main__':
    unittest.main(verbosity=2)