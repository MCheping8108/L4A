import pymongo
import datetime


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database66
    db.file.delete_many({})
    db.file.insert_many(
        [
            {'name': '头号文件', 'time': 1564020611.0},
            {'name': '财务报表', 'time': 1561435200.0},
            {'name': '安全事件', 'time': 1558674610.0},
            {'name': '领导指示', 'time': 1556244603.0},
            {'name': '金融走向', 'time': 1553566205.0},
            {'name': '内部安排', 'time': 1551183605.0},
        ]
    )

    return db


db = data_init()
