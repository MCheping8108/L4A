from flask import Flask, render_template, request, redirect, jsonify
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == '' or password == '':
        response = jsonify({'state': 'failure','msg':'用户名、密码都不能为空'})
    else:
        response = jsonify({'state': 'success','msg':'登录成功'})
        # 请在下方写你的代码：设置cookie,键为auto_login, 值为yes

    return response


@web.route('/login', methods=['GET'])
def login_page():
    # 请在下方写你的代码：获取cookie，如果为yes，则直接重定向到首页 /index

    
    return render_template('login.html')


@web.route('/index', methods=['GET'])
def home():
    return render_template('index.html')


web.run(host='127.0.0.1', port=5003)

