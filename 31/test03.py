# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)

# 使用school数据库
db = client['school']

# 请在下方写你的代码：删除数据库school
