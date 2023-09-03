import pymongo
from flask import request, jsonify, session, Blueprint, redirect

plant = Blueprint('plant', __name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.farm


# 实现种植功能
@plant.route('/plant/crop', methods=['GET'])
def plant_crop():
    username = session['username']
    # 获取请求传递的数据
    crop_name = request.args.get('crop')
    price = request.args.get('seed_price')
    land = request.args.get('land')
    plant = {'crop_name': crop_name, 'level': 0, 'seed_price': price}
    # 更新文档，种植植物
    db.user.update_one({'username': username},
                       {'$set': {land: plant}})
    # 更新金币数量，金币减少
    db.user.update_one({'username': username},
                       {'$inc': {'coins': -int(price)}})
    # 查找用户，取出剩余金币
    user = db.user.find_one({'username': username})
    coins = user['coins']

    # 返回响应
    return jsonify({'state': 'success', 'data': coins})


# 实现浇水功能
@plant.route('/plant/water', methods=['GET'])
def plant_water():
    username = session['username']
    # 获取土地
    land = request.args.get('land')
    # 查找用户，取出植物信息
    user = db.user.find_one({'username': username})
    plant = user[land]
    # 植物等级增加1
    plant['level'] = plant['level'] + 1
    # 更新植物等级
    db.user.update_one({'username': username},
                       {'$set': {land: plant}})
    # 更新文档，扣除金币
    db.user.update_one({'username': username},
                       {'$inc': {'coins': -2}})
    # 查找用户，取出剩余金币
    user = db.user.find_one({'username': username})
    coins = user['coins']

    # 返回响应
    return jsonify({'state': 'success', 'data': coins})


# 实现收获功能
@plant.route('/plant/harvest', methods=['GET'])
def plant_harvest():
    username = session['username']
    land = request.args.get('land')
    # 在下方写你的代码：查询用户信息，获取对应土地植物信息

    # 收获果实，更新金币数量，增加种子价格的2.5倍

    # 更新植物等级

    # 查询剩余金币
    result = db.user.find_one({'username': username})
    coins = result['coins']
    # 返回响应
    return jsonify({'state': 'success', 'data': coins})


# 实现铲除功能
@plant.route('/plant/eradicate', methods=['GET'])
def plant_eradicate():
    land = request.args.get('land')
    username = session['username']
    # 在下方写你的代码：删除农作物数据，更新土地land的值为空字典

    # 返回响应
    return jsonify({'state': 'success', 'data': None})
