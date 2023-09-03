from flask import Flask, render_template, request, redirect

web = Flask(__name__)

web.debug = True


@web.route('/login', methods=['GET'])
def login_page():
    # 在下方写你的代码:获取cookie并验证，如果是yes则重定向到首页

    return render_template('g_login.html')


@web.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email or password is "":
        return render_template('g_login.html')

    response = redirect('/')
    # 在下方写你的代码：设置cookie，键为auto_login,值为yes

    return response


@web.route('/', methods=['GET'])
def home():
    return render_template('g_home.html')


web.run(host='127.0.0.1', port=8001)
