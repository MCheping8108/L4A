from flask import Blueprint, render_template, session, redirect, request, jsonify
from config import db
from bson import ObjectId
import traceback

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
    # 使用一个新的集合保存用户的游戏记录
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

    try:
        user = session['user']
        # 在下方写你的代码：把字符串道具 id 转成 ObjectId 对象
        prop_id = request.args.get('prop_id')
        prop = db.props.find_one({'_id': prop_id})
        if user['coins'] < prop['price']:
            return jsonify({'data': '金币不足'})
        # 游戏数据更新
        # 在下方写你的代码：先查询数据库中是否有该用户游戏记录

        # 如果此前没有记录，则初始化用户的游戏记录

        record = {
            'user_id': ObjectId(user['_id']),
            'game_id': prop['game_id'],
            'power_level': 1,
            'shoot_level': 1,
            'life_level': 3
        }
        db.record.insert_one(record)

        # 再获取该道具的属性

        # 判断如果用户的属性级数小于道具数据最大级，则级数加1

            # 通过 user_id 和 game_id 来查找用户游戏记录，重置用户游戏记录为 record 变量

            # 消耗金币，更新user变量中的道具价格

            # 在 user 集合中更新金币数量

            # 重置 session

            # 返回“购买成功”
        return jsonify({'data': '购买成功'})
        # 如果用户的属性级数大于等于道具数据最大级，则返回“已经满级”

    except Exception as e:
        # 在下方写你的代码：打印详细的报错信息
        print('报错信息:%s' % e)
        return jsonify({'data': '服务端程序出错了！'})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
