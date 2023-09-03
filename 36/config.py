# 导入pymongo
import pymongo
# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 创建数据库
db = client['blog']


