import pymongo
from pprint import pprint

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database52
db.student.delete_many({})
db.composition.delete_many({})
db.student.insert_many(
    [
        {'name': '小明', 'age': 12, 'gender': '男'},
        {'name': '小美', 'age': 11, 'gender': '女'},
    ]
)
db.composition.insert_many(
    [
        {'name': '《博物馆》', 'date': '2018.7.15', 'content': '爸爸带我去博物馆看了好多飞机模型，非常棒...'},
        {'name': '《小狗》', 'date': '2018.7.16', 'content': '下雨了，在路上看到一只可怜的小狗在林雨，好想带它回'},
        {'name': '《快乐的一天》', 'date': '2018.7.17', 'content': '小伙伴们一起玩的很开心'}
    ]
)

# 下方写你的代码:找到作文名字为“《博物馆》”、“《小狗》”对应的文档
db.composition.find_one({'name': '《博物馆》'})
db.composition.find_one({'name': '《小狗》'})

# 构建“《博物馆》”、“《小狗》”的 id 列表
p1_id = db.composition.find_one({'name': '《博物馆》'})['_id']
p2_id = db.composition.find_one({'name': '《小狗》'})['_id']
composition_ids = [p1_id, p2_id]
db.student.update_one({'name': '小明'}, {'$set': {'composition': composition_ids}})

# 建立学生 小明 与作文之间的引入式关系
print(db.composition.update_many({'_id': {'$in': composition_ids}}, {'$set': {'student': '小明'}}))

print(db.student.find_one({'name': '小明'}))
print(db.composition.find_one({'name': '《博物馆》'}))


















