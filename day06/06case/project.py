# 从flask模块中导入request
from flask import Flask, render_template,request


project = Flask(__name__)


@project.route('/', methods=['GET'])
def baidu():
    return render_template('baidu.html')


@project.route('/search', methods=['GET'])
def search():
    # 在下方写你的代码：获取GET请求传递的数据
    key_words=request.args.get('kw')
    return '<h1>您搜索的关键词是："%s"</h1>' % key_words


project.run(host='127.0.0.1', port=8000)
