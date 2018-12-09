import requests
import unittest
import json
from conf import config
from lib.db import chack_user,del_user,up_card
from lib import load_data
from lib.case_log import log_case_info

class TestTiedCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,'绑卡')
    def test_tied_card_normal(self):
        case_data = load_data.get_case(self.sheet,'test_tied_card_normal')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url= url,json=data)
        log_case_info('test_tied_card_normal',case_data[2],case_data[3],case_data[4],res.json())
        print(res.json())
        self.assertDictEqual(excepted_res,res.json())
        # self.assertEqual(res.json()['msg'],'绑定成功')
        self.assertTrue(chack_user('victor12'))

        del_user('Victor12')
        up_card('6216600411129')

    def test_tied_card_wrong(self):
        case_data = load_data.get_case(self.sheet,'test_tied_card_wrong')
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        log_case_info('test_tied_card_wrong', case_data[2], case_data[3], case_data[4], res.json())
        print(res.json())
        self.assertDictEqual(excepted_res,res.json())
        # self.assertEqual(res.json()['msg'], '加油卡号不存在')
        # self.assertTrue(chack_user('Victor'))
if __name__ == '__main__':
    unittest.main(verbosity=2)
