# 请在下方写你的代码：导入pymongo
import pymongo

# 建立连接client
client = pymongo.MongoClient('127.0.0.1', 27017)

# 创建数据库disney
db = client['disney']

# 创建集合garage_kits
db.create_collection('garage_kits')


# 查看所有集合名称并打印
print(db.list_collection_names())
