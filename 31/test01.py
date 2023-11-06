# 请在下方写你的代码：连接数据库
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['school']
db.create_collection('student')
print(db)
