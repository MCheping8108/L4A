# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)

# 使用school数据库
db = client['school']

# 在下方写你的代码： 删除student集合并查看所有集合
db.drop_collection('student')

