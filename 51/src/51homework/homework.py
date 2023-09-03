import pymongo
import pprint

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database51
db.host.delete_many({})
db.pet.delete_many({})
db.host.insert_many(
    [
        {'name': '小云', 'age': 26, 'gender': '女'},
        {'name': '小明', 'age': 28, 'gender': '男'}
    ]
)
db.pet.insert_many(
    [
        {'name': '黑豆', 'age': 1, 'type': '田园犬'},
        {'name': 'lucky', 'age': 2, 'type': '金毛'},
        {'name': '亨利', 'age': 4, 'type': '金毛'},
        {'name': '爆米花', 'age': 1, 'type': '博美'},

    ]
)


# 下方写你的代码:找到宠物 黑豆 对应的文档，把它与主人 小云  建立嵌入式关系

pet = db.pet.find_one({'name': '黑豆'})
db.host.update_one({'name': '小云'}, {'$set': {'pet': [pet]}})

pprint.pprint(db.host.find_one({'name': '小云'}))

