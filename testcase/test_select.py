import requests
import unittest
import json
from conf import config
from lib import load_data
from lib.case_log import log_case_info
class TestSelect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,'查询')
    def test_select_normal(self):
        case_data = load_data.get_case(self.sheet,'test_select_normal')
        url = case_data[2]
        params = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.get(url=url,params=params)
        self.assertDictEqual(excepted_res, res.json())
        log_case_info('test_select_normal',case_data[2],case_data[3],case_data[4],res.json())
        print(res.json())
        # self.assertEqual(res.text['msg'],'成功返回')
        # self.assertIs(res.text['code'],200)

    def test_select_wrong(self):
        case_data = load_data.get_case(self.sheet,'test_select_wrong')
        url = case_data[2]
        params = json.loads(case_data[3])
        # url = 'http://115.28.108.130:8080/gasStation/process'
        # params = {"dataSourceId":"bHRz",
        #           "userId":"8564",
        #           "cardNumber":"6216600411124",
        #           "methodId":"02A"}
        excepted_res = json.loads(case_data[4])
        res = requests.get(url=url,params=params)
        self.assertDictEqual(excepted_res,res.json())
        log_case_info('test_select_wrong',case_data[2],case_data[3],case_data[4],res.json())
        print(res.json())
        # self.assertEqual(res.json()['msg'],'无查询信息')
        # self.assertEqual(res.json()['code'],400)
if __name__ == '__main__':
    unittest.main(verbosity=2)
