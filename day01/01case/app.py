# 从flask模块中导入Flask类
from flask import Flask

# 创建flask对象app
app = Flask(__name__)


# 设置访问的路径
@app.route('/hello')
def hello():
    # 返回响应内容
    return 'Hello,World!'


# 启动服务器程序
app.run(host='127.0.0.1',port=8000)