from flask import Flask, url_for, redirect, render_template, request

web = Flask(__name__)

web.debug = True


@web.route('/lego/index', methods=['GET'])
def home():
    return render_template('lego_home.html')


@web.route('/lego/login', methods=['GET'])
def login_page():
    return render_template('lego.html')


@web.route('/lego/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 请在下方写你的代码:当用户名密码正确，则重定向到首页


web.run(host='127.0.0.1', port=8001)
