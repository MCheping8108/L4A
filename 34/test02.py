from data_init import db

# 更新前查询
for r in db.star.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新肖战的粉丝数


# 更新后查询
for r in db.star.find():
    print(r)
