import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database41
db.scenery.remove({})
db.scenery.insert_many(
    [
        {'name': '迪士尼乐园', 'address': '香港'},
        {'name': '故宫', 'address': '北京'},
        {'name': '长城', 'address': '北京'},
        {'name': '黄山', 'address': '安徽'},
        {'name': '泰山', 'address': '山东'},
        {'name': '乐山大佛', 'address': '四川'},
        {'name': '三亚', 'address': '海南'},
        {'name': '丽江', 'address': '云南'},
        {'name': '苏州园林', 'address': '江苏'},
        {'name': '东方明珠', 'address': '上海'},
    ]
)
# 亲自出码，在下方写你的代码：查询文档，并把所有的ObjectId对象转为字符串

