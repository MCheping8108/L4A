from flask import Blueprint, request, jsonify, session, redirect
from config import db

user = Blueprint('user', __name__)


# 实现登录功能
@user.route('/login', methods=['POST'])
def signin():
    # 接收前端发送的用户名 username 以及密码 password
    username = request.form.get('username')
    password = request.form.get('password')
    # 根据用户名在 user 集合中查询用户信息
    user = db.user.find_one({'username': username})
    # 如果不存在该用户信息，则返回响应，状态 code 为 1，提示信息 data 为：用户名不存在
    if user is None:
        return jsonify({'code': 1, 'data': '用户名不存在'})
    # 如果用户输入的密码和数据库中存储的密码不一致，则返回响应，状态 code 为 1，提示信息 data 为：密码不正确
    if user['password'] != password:
        return jsonify({'code': 1, 'data': '密码不正确'})
    # 把用户文档 user 中的 ObjectId 对象转为字符串
    user['_id'] = str(user['_id'])
    # 在 session 中保存用户信息 user
    session['user'] = user
    # 返回响应：状态 code 为 0 ，提示信息 data 为: 登录成功
    return jsonify({'code': 0, 'data': '登录成功'})


@user.route('/register', methods=['POST'])
def signup():
    # 接收用户名和密码
    username = request.form.get('username')
    password = request.form.get('password')
    # 接收前端发送的确认密码 password
    repassword = request.form.get('repassword')
    # 如果用户名、密码、确认密码都为空
    if username is '' or password is ''or repassword is '':
        # 则返回响应，状态 code 为 1，提示信息：参数错误
        return jsonify({'code': 1, 'data': '参数错误'})
    # 验证用户名
    if db.user.find_one({'username': username}) is not None:
        return jsonify({'code': 1, 'data': '用户名已被注册'})
    # 如果密码和确认密码不一致，则返回响应，状态 code 为 1，提示信息：两次密码不一致
    if password != repassword:
        return jsonify({'code': 1, 'data': '两次密码不一致'})
    db.user.insert_one({'username': username, 'password': password})
    return jsonify({'code': 0, 'data': '注册成功'})
