#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'longtengserver'
db_charset = 'utf8'

#路劲配置
# __name__运行模块名字
# __file__当前路劲

import os

config_path = os.path.abspath(__file__)  # 绝对路径
data_path = os.path.dirname(os.path.abspath(__file__))  # 文件路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路劲
log_file = os.path.join(project_path, 'log', 'log.txt')
data_file = os.path.join(project_path,'data','data.xlsx')
report_file = os.path.join(project_path,'report','reoprt.html')



#日志
import logging
logging.basicConfig(level=logging.DEBUG,
                    format= "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt = "%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a"
                    )

if __name__ == "__main__":
    logging.info("hello,world")
    # print(os.path.abspath(__file__))#绝对路径
    # print(os.path.dirname(os.path.abspath(__file__)))#文件路径
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#项目路劲
    # print(os.path.join(project_path,'log','log.txt'))
    # print(os.path.join(project_path,'data','data.xlsx'))
    # print(os.path.join(project_path,'report','reoprt.html'))

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '624424010@qq.com'
smtp_password = 'Victor929115'

receiver = '963570929@qq.com'
subject = '接口测试报告'
body = 'hi,all,\n附件中是解救测试报告，请查收'

