from flask import Blueprint, render_template, redirect, request, jsonify, session
from config import db

bp = Blueprint('user', __name__)

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'xiaotong', 'password': '123456'},
    {'id': '2', 'username': 'xiaomei', 'password': '000000'},
    {'id': '3', 'username': 'xiaoming', 'password': '888888'}
]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    # 在下方写你的代码：在user集合中查询指定用户名文档，并不返回_id键
    users = list(db.user.find({'username': username}, {'_id': 0}))
    for user in users:
        if user['username'] == username:
            return user
    return None


@bp.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 获取Cookie中保存的上次登录的用户名
        username = request.cookies.get('username', '')

        # 如果已登录则重定向到首页
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

        # 将用户信息保存在session中
        session['user'] = user

        # 获取redirect函数返回的Response对象
        response = redirect('/')
        # 将用户名保存在Cookie中
        response.set_cookie('username', username, max_age=600)

        # 登录成功，重定向到首页
        return response


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

        # 注册成功，保存在字典中（之前的逻辑）
        # user = {'id': len(users) + 1, 'username': username, 'password': password}
        # users.append(user)

        # 在下方写你的代码：构建用户信息字典
        user = {
            'username': username,
            'password': password,
            'head': '1.jpg',
            'coins': 0
        }

        # 将注册信息插入到集合user中
        # db.create_collection('user')
        db.user.insert_one(user)


        # 注册成功，重定向到登录页
        return jsonify({'status': 'success', 'msg': '恭喜注册成功'})
