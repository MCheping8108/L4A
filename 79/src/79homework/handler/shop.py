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
    # 从 session 中获取用户信息 user
    user = session.get('user')
    # 获取前端传递的商品类别id
    category_id = ObjectId(request.args.get('category_id'))
    # 根据商品类别 id 查询该商品类别的文档
    category = db.category.find_one({'_id': category_id})
    # 从商品类别文档中获取该类别下的所有商品id，然后遍历
    products = []
    for pid in category['products']:
        # 根据商品 id 查询商品详情，并把其添加到列表中
        p = db.product.find_one({'_id': pid})
        products.append(p)
    # 返回响应，渲染 detail.html，返回用户信息 user 和 商品详情 products
    return render_template('detail.html', user=user, products=products)


# 添加商品到购物车
@shop.route('/add', methods=['GET'])
def add_to_cart():
    if not session.get('user'):
        return jsonify({'code': 1, 'data': '请先登录'})
    # 从 session 中获取用户信息 user
    user = session.get('user')
    # 获取用户 id
    user_id = ObjectId(user['_id'])
    # 获取前端传递的商品 id 并转为 ObjectId 对象
    product_id = ObjectId(request.args.get('product_id'))
    # 查询用户购物车内是否有未付款的该商品
    product = db.cart.find_one({'user_id': user_id, 'product_id': product_id, 'status': 0})
    # 如果不存在，则该商品为第一次添加
    if product == None:
        # 在 cart 集合中添加一条新文档，内容包括：用户id：user_id，商品id：product_id，数量 amount:初始值为1，付款状态status：0
        record = {
            'user_id': user['_id'],
            'product_id': product_id,
            'amount': 1,
            'status': 0
        }
        db.cart.insert_one(record)
    # 在下方写你的代码：如果购物车内有该商品，表示该商品已经添加过了，只需要把商品数量加 1 即可

    return jsonify({'code': 0, 'data': '添加购物车成功'})




