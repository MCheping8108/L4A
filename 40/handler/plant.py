import pymongo
from flask import request, jsonify, session, Blueprint, redirect

plant = Blueprint('plant', __name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.farm


# 实现种植功能
@plant.route('/plant/crop', methods=['GET'])
def plant_crop():
    username = session['username']

    # 在下方完成代码
    crop_name = request.args.get('crop')
    price = request.args.get('seed_price')
    land = request.args.get('land')
    plant = {'crop_name': crop_name, 'level': 0, 'seed_price': price}
    db.user.update_one({'username': username}, {'$set': {land: plant}})
    db.user.update_one({'username': username}, {'$inc': {'coins': -int(price)}})

    # 查找用户，取出剩余金币
    user = db.user.find_one({'username': username})
    coins = user['coins']
    # 移除pass，在此返回响应
    return jsonify({'state': 'success', 'data': None})

# 实现浇水功能
@plant.route('/plant/water', methods=['GET'])
def plant_water():
    username = session['username']
    # 获取土地
    land = request.args.get('land')

    # 在下方完成代码:
    user = db.user.find_one({'username': username})
    plant = user[land]
    plant['level'] = plant['level'] + 1
    db.user.update_one({'username': username}, {'$set': {land: plant}})
    db.user.update_one({'username': username}, {'$inc': {'coins': -2}})

    
    # 查找用户，取出剩余金币
    user = db.user.find_one({'username': username})
    coins = user['coins']

    # 返回响应
    return jsonify({'state': 'success', 'data': coins})
