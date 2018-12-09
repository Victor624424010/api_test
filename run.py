import unittest
from conf import config
from lib.emailtest import send_report
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
#遍历指定文件夹下及子包的所有用例test
suite = unittest.defaultTestLoader.discover('./testcase')
# unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(suite)
    config.logging.info('测试开始'+'='*50)
    with open (config.report_file,'wb') as f:
        HTMLTestRunner(stream=f,title='User接口测试报告',description='测试报告').run(suite)
    if config.is_send_report:
        send_report()
        config.loging.info()

