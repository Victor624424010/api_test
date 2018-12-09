import unittest
import requests
import json
from conf import config
from lib import load_data
from lib.case_log import log_case_info
class TestExpence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,'消费')
    def test_expevce_normal(self):
        case_data = load_data.get_case(self.sheet,'test_expevce_normal')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url,json=data)
        print(res.json())
        log_case_info('test_expevce_normal',case_data[2],case_data[3],case_data[4],res.json())
        self.assertDictEqual(excepted_res,res.json())

        # self.assertEqual(res.json()['msg'],'消费成功!')
        # self.assertEqual(res.json()['code'], 200)

    def test_expevce_wrong(self):
        case_data = load_data.get_case(self.sheet,'test_expevce_wrong')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url,json=data)
        print(res.json())
        log_case_info('test_expevce_wrong',case_data[2],case_data[3],case_data[4],res.json())
        self.assertDictEqual(excepted_res,res.json())
        # self.assertEqual(res.json()['msg'],'根据用户ID没有查询到卡号!')
        # self.assertEqual(res.json()['code'], 5013)
if __name__ == '__main__':
    unittest.main(verbosity=2)
