import pymongo
from bson import ObjectId
from pprint import pprint

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database53
db.students.delete_many({})
db.book.delete_many({})
db.students.insert_many(
    [
        {'_id': ObjectId('5fa206d569ad710c9c842b01'), 'name': '小程', 'age': 12, 'gender': '男',
         'bookId': [ObjectId('5fa206d569ad710c9c842b04')]},
        {'_id': ObjectId('5fa206d569ad710c9c842b02'), 'name': '小美', 'chairman': '丁磊', 'time': '1997年6月',
         'gameId': [ObjectId('5fa206d569ad710c9c842b05')]}
    ]
)
db.book.insert_many(
    [
        {'_id': ObjectId('5fa206d569ad710c9c842b03'), 'name': '爱的教育', 'author': '埃·德·亚米契斯'},
        {'_id': ObjectId('5fa206d569ad710c9c842b04'), 'name': '钢铁是怎样炼成的', 'author': '尼古拉·阿列克谢耶维奇·奥斯特洛夫斯基斯'},
        {'_id': ObjectId('5fa206d569ad710c9c842b05'), 'name': '安徒生童话', 'author': '汉斯·克里斯蒂安·安徒生'},
    ]
)

# 更新前，打印 name 是小程的文档
pprint(db.students.find_one({'name': '小程'}))
print('='*50)

# 下方写你的代码:查询书籍'爱的教育'的id，把他添加到'小程'已看书籍列表中


# 更新前，打印 name 是小程的文档
pprint(db.students.find_one({'name': '小程'}))
