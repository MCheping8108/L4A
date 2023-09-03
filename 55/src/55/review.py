import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database55
d1 = list(db.diner.find())
if len(d1) <= 0:
    db.diner.insert_many(
        [
            {'_id': ObjectId('5f1bb18269ad715d184065b2'), 'name': '莉莉', 'gender': '女',
             'dineId': [ObjectId('5f1bb18269ad715d184065b6'), ObjectId('5f1bb18269ad715d184065b7')], },
            {'_id': ObjectId('5f1bb18269ad715d184065b3'), 'name': '美美', 'gender': '女',
             'dineId': [ObjectId('5f1bb18269ad715d184065b5'), ObjectId('5f1bb18269ad715d184065b7')]},
            {'_id': ObjectId('5f1bb18269ad715d184065b4'), 'name': '可心', 'gender': '女',
             'dineId': [ObjectId('5f1bb18269ad715d184065b9'), ObjectId('5f1bb18269ad715d184065b7')]},
            {'_id': ObjectId('5f1bb18269ad715d184065b5'), 'name': '安安', 'gender': '女',
             'dineId': [ObjectId('5f1bb18269ad715d184065b7'), ObjectId('5f1bb18269ad715d184065b8')]},
        ]
    )
d2 = list(db.restaurant.find())
if len(d2) <= 0:
    db.restaurant.insert_many(
        [
            {'_id': ObjectId('5f1bb18269ad715d184065b6'), 'name': '西餐厅', 'address': '红旗路8号', 'phone': 15538027041},
            {'_id': ObjectId('5f1bb18269ad715d184065b7'), 'name': '肯德基', 'address': '解放路18号', 'phone': 17588067051},
            {'_id': ObjectId('5f1bb18269ad715d184065b8'), 'name': '绿茶餐厅', 'address': '迎宾路13号', 'phone': 15830027031},
            {'_id': ObjectId('5f1bb18269ad715d184065b9'), 'name': '外婆家餐厅', 'address': '百花路22号', 'phone': 13232027840}
        ]
    )
# 在下方写你的代码：查询莉莉都去过哪些餐厅

