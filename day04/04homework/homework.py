from flask import Flask, render_template

myweb = Flask(__name__)

# 开启调试模式
myweb.debug = True

# 设置静态文件缓存过期时间
myweb.send_file_max_age_default = 1

# 设置模板文件存放路径
# myweb.j




@myweb.route('/favicon.ico')
def get_fav():
    return myweb.send_static_file('images/favicon.ico')

# 请在下方写你的代码：设置动态路由，返回对应的pony或者series页面
@myweb.route('/pony/<name>')
def get_pony(name):
    return render_template('pony.html')
@myweb.route('/series/<name>')
def get_series(name):
    return render_template('series.html')



myweb.run(host='127.0.0.1', port=5000)
