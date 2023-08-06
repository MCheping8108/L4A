from flask import Flask

myweb = Flask(__name__)
myweb.debug=True

@myweb.route('/favicon.ico')
def get_fav():
    return myweb.send_static_file('image/favicon.ico')

# 请在下方写你的代码
# 设置动态路由
@myweb.route('/<num>')
def home(num):
    num = int(num)
    square = num*num
    return '%d * %d=%d' % (num, num, square)


myweb.run(host='127.0.0.1', port=8001)
