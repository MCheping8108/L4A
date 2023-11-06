# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 创建数据库
db = client['database32']


# 在下方写你的代码：查询student集合中的所有文档
result = db.student.find()
student=list(result)
print(student)






