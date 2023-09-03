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
