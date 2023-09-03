from flask import Blueprint, render_template, session, request, jsonify, redirect
from config import db
from bson import ObjectId

shop = Blueprint('shop', __name__)


# 实现首页
@shop.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# 统计购物车商品总数
@shop.route('/count', methods=['GET'])
def get_cart_count():
    if not session.get('user'):
        return jsonify({'code': 1, 'data': '请先登录'})
    user = session.get('user')
    count = db.cart.find({'user_id': ObjectId(user['_id']), 'status': 0}).count()
    return jsonify({'code': 0, 'data': count})

