# 从flask模块中导入Flask类，render_template函数
from flask import Flask, render_template

# 创建flask对象app
app = Flask(__name__)

# 开启调试模式
app.debug = True


# 设置路由
@app.route('/')
def index():
    # 返回响应
    return render_template('index.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
