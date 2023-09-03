import pymongo


def data_init():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['database34']

    if not db.child.find_one():
        # 初始化时插入数据
        children = [
            {'name': '小丽', 'pocket_money': 150},
            {'name': '小明', 'pocket_money': 100}
        ]
        db.child.insert_many(children)
    return db


db = data_init()

# 更新前查询
for r in db.child.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新字段 pocket_money 的值


# 更新后查询
for r in db.child.find():
    print(r)
