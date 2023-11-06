# 请在下方写你的代码: 创建数据库blog
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['blog']
db.create_collection('article')
print(db)
