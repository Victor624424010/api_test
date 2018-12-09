#导入
from flask import Flask,request
#用当前模块实例化一个Flask对象
app = Flask(__name__)
#写函数
@app.route('/add',methods=['GET','POST'])
def add():
    a = request.values.get('a')
    b = request.values.get('b')
    return str(int(a)+int(b))
#挂载接口路径，指定请求数据
#运行
app.run()