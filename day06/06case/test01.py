# 从flask模块中导入request
from flask import Flask, render_template,request

web = Flask(__name__)


@web.route('/', methods=['GET'])
def index():
    return render_template('order.html')


@web.route('/order', methods=['GET'])
def order():
    # 在下方写你的代码：获取GET请求传递的数据
    key_words=request.args.get('kw')
    # 返回响应 您已经成功点餐
    return '<h1>您已经成功点餐："%s"</h1>' % key_words


web.run(host='127.0.0.1', port=8001)