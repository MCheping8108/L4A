import pymongo


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database57
    db.student.delete_many({})
    db.student.insert_many(
        [
            {'name': '周明', 'age': 10, 'gender': '男'},
            {'name': '王涵', 'age': '', 'gender': '女'},
            {'name': '赵佳佳', 'age': 10, 'gender': '女'},
            {'name': '陈子瑜', 'age': 11, 'gender': '男'},
            {'name': '马笑笑', 'age': 9, 'gender': '男'},
            {'name': '朱子玉', 'age': 10, 'gender': '女'},
            {'name': '龚明宏', 'age': 11, 'gender': '男'},
            {'name': '崔亮', 'age': 10, 'gender': '男'},
            {'name': '牛小龙', 'age': 9, 'gender': '男'},
            {'name': '钱欣欣', 'age': 9, 'gender': '女'},
            {'name': '孙美丽', 'age': 10, 'gender': '女'},
            {'name': '李嘉欣', 'age': 11, 'gender': '女'},
            {'name': '刘迪', 'age': 11, 'gender': '女'},
            {'name': '夏筱筱', 'age': 10, 'gender': '女'},
            {'name': '马明伟', 'age': 10, 'gender': '男'},
            {'name': '张子涵', 'age': 9, 'gender': '女'},
            {'name': '王凌琳', 'age': 11, 'gender': '女'},
            {'name': '王文静', 'age': 9, 'gender': '女'},
        ]
    )
    return db


db = data_init()
