import pymongo
from bson import ObjectId


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database54
    db.student.delete_many({})
    db.idol.delete_many({})
    db.student.insert_many(
        [
            {'_id': ObjectId('5d455fa8dfe943ba589ff3c8'), 'name': '李帅', 'gender': '男',
             'idolId': [ObjectId('5d455f83840181687059de13'), ObjectId('5d455f83840181687059de14')]},
            {'_id': ObjectId('5d455fa8dfe943ba589ff3c9'), 'name': '宋琪', 'gender': '女',
             'idolId': [ObjectId('5d455f83840181687059de13'), ObjectId('5d455f83840181687059de15')]},
            {'_id': ObjectId('5d455fa8dfe943ba589ff3ca'), 'name': '刘洋', 'gender': '男',
             'idolId': [ObjectId('5d455f83840181687059de13'), ObjectId('5d455f83840181687059de14'),
                        ObjectId('5d455f83840181687059de15')]}
        ]
    )

    db.idol.insert_many(
        [
            {'_id': ObjectId('5d455f83840181687059de13'), 'name': '王俊凯', 'flowers': '24.5万'},
            {'_id': ObjectId('5d455f83840181687059de14'), 'name': '杨紫', 'flowers': '24.3万'},
            {'_id': ObjectId('5d455f83840181687059de15'), 'name': '易烊千玺', 'flowers': '17.9万'}
        ]

    )
    return db


db = data_init()
