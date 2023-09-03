from flask import Flask,render_template, request,redirect

web = Flask(__name__)

web.debug = True


@web.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@web.route('/index', methods=['GET'])
def home():
    return render_template('index.html')


@web.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 请在下方写你的代码:验证用户名和密码正确之后，重定向到首页/index，否则重定向到登录页/login。
    if username == 'xiaotong' and password == '123456':
        return redirect('/index')
    else:
        return redirect('/login')


web.run(host='127.0.0.1', port=5000)



















