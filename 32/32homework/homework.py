# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 创建数据库
db = client['database32']

# 插入数据
db.cartoon.insert_many([
    {'name': '名侦探柯南', 'country': '日本', 'type': '推理'},
    {'name': '斗罗大陆', 'country': '中国', 'type': '奇幻'},
    {'name': '海贼王', 'country': '日本', 'type': '冒险'},
    {'name': '网球王子', 'country': '日本', 'type': '体育'},
])

# 在下方写你的代码：查询出 “名侦探柯南”这条文档，并且不返回"_id"键
result = db.cartoon.find_one({'name': '名侦探柯南'}, {'_id': 0})
print(result)

