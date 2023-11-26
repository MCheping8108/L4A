from data_init import db

# 更新前查询
for r in db.student.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新马云数学的成绩为19
db.student.update_one({'name': '马云'}, {'$set': {'math': 19}})

# 盖茨、特朗普的年级都改为3年级
db.student.update_many({'name': {'$in': ['盖茨', '特朗普']}}, {'$set': {'grade': '3年级'}})


# 更新后查询
for r in db.student.find():
    print(r)
