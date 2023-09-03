from config import db,data_import

#初始化数据
data_import()

# 更新前查询
for r in db.stu.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新Tom完成的作业


# 更新后查询
for r in db.stu.find():
    print(r)
