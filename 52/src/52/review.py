import pymongo
import pprint

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['database52']
db.classes.delete_many({})
db.monitor.delete_many({})
db.classes.insert_many(
    [
        {'className': '三年级(2)班', 'number': 50},
        {'className': '三年级(1)班', 'number': 48},
        {'className': '二年级(1)班', 'number': 49},
    ]
)
db.monitor.insert_many(
    [
        {'name': '王安', 'gender': '男', 'age': 9},
        {'name': '李月月', 'gender': '女', 'age': 8},
        {'name': '张峰', 'gender': '男', 'age': 9}
    ]
)

if __name__ == '__main__':
    pass
    # 在下方你的代码：查看王安文档的id

    # 建立班级和班长的嵌入式关系，即更新三年级(2)班的文档信息，增加字段monitor，值就是班长的文档

    # 查询三年(2)班的文档信息并打印
