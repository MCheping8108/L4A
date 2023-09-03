from flask import Blueprint, render_template, session, redirect, request, jsonify
from config import db
from bson import ObjectId

bp = Blueprint('game', __name__)


# 游戏页面
@bp.route('/game')
def game():
    if not session.get('user'):
        return redirect('/user/login')
    user = session['user']
    games = list(db.game.find({}))
    return render_template('game.html', user=user, games=games)


# 商店页面
@bp.route('/store', methods=['GET'])
def store_index():
    if not session.get('user'):
        return redirect('/user/login')
    user = session['user']
    props = list(db.props.find({}))
    return render_template('store.html', user=user, props=props)


# 飞机大战页面
@bp.route('/game/plane_war', methods=['GET'])
def game_plane_war():
    if not session.get('user'):
        return redirect('/user/login')
    user = session['user']
    user_id = ObjectId(user['_id'])
    game_id = ObjectId(request.args.get('id'))
    # 使用一个新的集合保存用户的购买记录
    record = db.record.find_one({'user_id': user_id, 'game_id': game_id})
    if record == None:
        record = {
            'user_id': user_id,
            'game_id': game_id,
            'power_level': 1,
            'shoot_level': 1,
            'life_level': 3
        }
        db.record.insert_one(record)
    return render_template('/game/plane.html', record=record)


# 购买道具
@bp.route('/store/buy', methods=['GET'])
def store_buy():
    if not session.get('user'):
        return redirect('/user/login')
    # 从 session 中获取用户信息
    user = session['user']
    # 获取请求参数商品id
    prop_id = request.args.get('prop_id')
    # 根据商品 id 查询商品文档
    prop = db.props.find_one({'_id': prop_id})
    if user['coins'] < prop['price']:
        return jsonify({'data': '金币不足'})
    # 在下方写你的代码：购买商品后，添加游戏装备等级

    # 在数据库中插入游戏装备等级记录

    # 返回提示信息“购买成功”









