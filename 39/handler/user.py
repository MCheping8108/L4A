import pymongo
from flask import render_template, request, jsonify, session, Blueprint, redirect

user = Blueprint('user', __name__)
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['farm']


@user.route('/user/register', methods=['GET'])
def register_page():
    return render_template('register.html')


@user.route('/user/login', methods=['GET'])
def login_page():
    return render_template('login.html')


# 在下方完成代码：实现注册功能
@user.route('/user/register', methods=['POST'])
def register():
    # 获取用户名、密码
    username = request.form.get('username')
    password = request.form.get('password')
    # 判断用户名、密码是否为空
    if username == '' or password == '':
        return render_template('register.html', msg='用户名、密码不能为空')

    # 查询用户名对应的文档
    user = db.user.find_one({'username': username})
    # 若用户名已注册，返回带提示信息的注册页面
    if user:
        return render_template('register.html', msg='该用户名已被注册')
    # 保存用户名、密码到数据库
    db.user.insert_one({'username': username, 'password': password, 'coins': 100})
    # 重定向到登录页
    return redirect('/user/login')

def get_user():
    """
    返回用户的所有信息
    :return:
    """
    username = session['username']
    one = db.user.find_one({'username': username})
    result = {"username": one['username'], "coins": one['coins'], "crops": []}
    # 遍历获取所有植物，存到list中
    for key in one:
        if "land" in key and one[key]:
            crop = one[key]
            result['crops'].append(
                {"land": key[-1], "name": crop['crop_name'], "level": crop['level'], "seed_price": crop['seed_price']})
    return result
