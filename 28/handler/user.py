from flask import Blueprint, render_template, redirect, request, jsonify, session
# 请在下方写你的代码：创建user蓝图
bp = Blueprint('user', __name__)
@bp.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 获取提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断用户名是否已存在
        user = find(username)
        if user is not None:
            return jsonify({'status': 'failure', 'msg': '该用户名已被注册'})

        # 注册成功，保存在字典中
        user = {'id': len(users) + 1, 'username': username, 'password': password}
        users.append(user)
        # 日志打印登录用户
        # logging.info('登录用户' + str(user))

        # 注册成功，重定向到登录页
        return jsonify({'status': 'success', 'msg': '恭喜注册成功'})
@bp.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 获取Cookie中保存的上次登录的用户名
        username = request.cookies.get('username', '')

        # 在下方写你的代码：获取session,如果存在，则重定向到首页
        if session.get('user'):
            print(session.get('user').get('username'))
            return redirect('/')

        return render_template('login.html', username=username)
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = find(username)
        if user is None:
            return render_template('login.html', username=username, user_msg='用户名不存在')
        if user['password'] != password:
            return render_template('login.html', username=username, pass_msg='密码错误，请重试')

        # 登录成功后，把用户信息存储到session中
        session['user'] = user
        # 日志打印登录用户
        # logging.info('登录用户' + str(user))
        # 获取redirect函数返回的Response对象
        response = redirect('/')
        # 将用户名保存在Cookie中
        response.set_cookie('username', username, max_age=600)
        # 登录成功，重定向到首页
        return response