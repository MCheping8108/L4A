import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database46
db.flowers.delete_many({})
db.flowers.insert_many(
    [
        {'_id': ObjectId('5d31a04c84722d28bf28add6'), 'name': '月季花', 'type': '木本花卉', 'time': '夏季'},
        {'_id': ObjectId('5d31a04c84722d28bf28add7'), 'name': '梅花', 'type': '木本花卉', 'time': '冬季'},
        {'_id': ObjectId('5d31a04c84722d28bf28add8'), 'name': '风信子', 'type': '木本花卉', 'time': '春季'},
        {'_id': ObjectId('5d31a04c84722d28bf28add9'), 'name': '水仙花', 'type': '草本花卉', 'time': '冬季'},
        {'_id': ObjectId('5d31a04c84722d28bf28adda'), 'name': '满天星', 'type': '草本花卉', 'time': '春季'},
        {'_id': ObjectId('5d31a04c84722d28bf28addb'), 'name': '菊花', 'type': '草本花卉', 'time': '秋季'},
        {'_id': ObjectId('5d31a04c84722d28bf28addc'), 'name': '玫瑰', 'type': '木本花卉', 'time': '夏季'},
        {'_id': ObjectId('5d31a04c84722d28bf28addd'), 'name': '芍药', 'type': '草本花卉', 'time': '春季'},
        {'_id': ObjectId('5d31a04c84722d28bf28adde'), 'name': '杜鹃花', 'type': '木本花卉', 'time': '春季'},
        {'_id': ObjectId('5d31a04c84722d28bf28addf'), 'name': '丁香花', 'type': '木本花卉', 'time': '春季'},
    ]
)
id = '5d31a04c84722d28bf28add6'
# 在下方写你的代码：将id转为ObjectId对象，然后在flowers集合中查询对应的文档
data = db.flowers.find_one({'_id': ObjectId(id)})
print(data)
