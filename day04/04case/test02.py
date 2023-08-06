from flask import Flask

myweb = Flask(__name__)


# 请在下方写你的代码
# 注册动态路由
@myweb.route('/<name>')
def index(name):
    # 返回响应
    return '<h1>hello,%s </h1>' % name


myweb.run(host='127.0.0.1', port=8002)
