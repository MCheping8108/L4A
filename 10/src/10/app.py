import ssl
from flask import Flask, render_template, request
import tools

ssl._create_default_https_context = ssl._create_unverified_context
# 创建web应用
app = Flask(__name__)
# 开启debug模式
app.debug = True


# 创建视图函数，注册路由/star
@app.route('/star', methods=['GET'])
def star():
    # 获取星座数据
    stars = tools.star_list()
    return render_template('star_home.html', stars=stars)


# @app.route('/china', methods=['GET'])
# def china():
#     return 苏联


# 在下方写你的代码:注册路由/star/fortune
@app.route('/star/fortune')
def star_fortune():
    # 获取选择的星座
    star = request.args.get('star')
    # return star
    # 获取详细星座运势信息
    star_fortune = tools.star_fortune(star)
    # 传递星座运势信息
    return render_template('star_fortune.html', fortune=star_fortune)

# 启动服务器
app.run(host='127.0.0.1', port=9000)
