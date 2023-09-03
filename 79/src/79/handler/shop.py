from flask import Blueprint, render_template, session, request, jsonify, redirect
from config import db
from bson import ObjectId

shop = Blueprint('shop', __name__)


# 实现首页
@shop.route('/', methods=['GET'])
def home():
    user = session.get('user')
    products = list(db.product.find({}).limit(8))
    return render_template('index.html', user=user, products=products)


# 统计购物车商品总数
@shop.route('/count', methods=['GET'])
def get_cart_count():
    if not session.get('user'):
        return jsonify({'code': 1, 'data': '请先登录'})
    user = session.get('user')
    count = db.cart.find({'user_id': ObjectId(user['_id']), 'status': 0}).count()
    return jsonify({'code': 0, 'data': count})


# 商品详情
@shop.route('/detail', methods=['GET'])
def detail():
    # 在下方写你的代码：从 session 中获取用户信息 user
    pass
    # 获取前端传递的商品类别id

    # 根据商品类别 id 查询该商品类别的文档

    # 从商品类别文档中获取所有商品id列表，然后遍历

        # 根据商品 id 查询商品详情，并把其添加到列表中

    # 返回响应，渲染 detail.html，返回用户信息 user 和 商品详情 products


# 添加商品到购物车
@shop.route('/add', methods=['GET'])
def add_to_cart():
    if not session.get('user'):
        return jsonify({'code': 1, 'data': '请先登录'})
    # 在下方写你的代码：从 session 中获取用户信息 user

    # 获取用户 id

    # 获取前端传递的商品 id 并转为 ObjectId 对象

    # 查询用户购物车内是否有未付款的该商品

    # 如果不存在，则该商品为第一次添加

        # 在 cart 集合中添加一条新文档，内容包括：用户id：user_id，商品id：product_id，数量 amount:初始值为1，付款状态status：0

    # 返回响应 code为 0 表示请求成功，data 提示信息为：添加购物车成功




