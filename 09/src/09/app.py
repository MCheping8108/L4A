import ssl
import tools
# 导入 Flask 类
# import flask, render_template
from flask import Flask, render_template

ssl._create_default_https_context = ssl._create_unverified_context

# 创建web应用
web = Flask(__name__)
# 开启debug模式
web.debug = True
# 创建视图函数，注册路由/star
@web.route('/star')
def star():
      stars = tools.star_list()
      return render_template('star_home.html', stars=stars)

# @web.route('/star_list')
# def star_list():
#       return tools.star_list()
      
# 启动服务器
web.run(host='localhost', port=8000)

print('server running at http://localhost:8000')