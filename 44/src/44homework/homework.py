import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database44
db.sports.delete_many({})
db.sports.insert_many(
    [
        {"name": "足球", "people": 11, "origin": "中国"},
        {"name": "篮球", "people": 5, "origin": "美国"},
        {"name": "乒乓球", "people": 2, "origin": "英国"},
        {"name": "网球", "people": 2, "origin": "英国"},
        {"name": "排球", "people": 6, "origin": "美国"},
        {"name": "橄榄球", "people": 11, "origin": "英国"},
        {"name": "冰球", "people": 6, "origin": "加拿大"},
        {"name": "曲棍球", "people": 11, "origin": "英国"},
        {"name": "羽毛球", "people": 2, "origin": "英国"},
        {"name": "保龄球", "people": 1, "origin": "德国"},
        {"name": "台球", "people": 2, "origin": "西欧"},
        {"name": "高尔夫球", "people": 1, "origin": "苏格兰"},
        {"name": "棒球", "people":9 , "origin": "英国"},
    ]
)

# 查询所有文档并循环打印
for s in db.sports.find():
    print(s)
print('='*100) 
   
# 在下方写你的代码：跳过sports集合中的前三条文档(将数据打印在控制台即可)























