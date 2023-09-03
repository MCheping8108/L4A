# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 创建数据库
db = client['database32']

# 在下方写你的代码：构建文档，并向集合中插入该文档
