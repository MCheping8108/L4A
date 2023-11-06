# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 创建数据库
db = client['database32']

bson = {'name': 'Tom', 'age': 9}

# 在下方写你的代码：插入一条文档
db.student.insert_one(bson)
print(db)