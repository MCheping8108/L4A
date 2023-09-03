from data_init import db

# 更新前查询
for r in db.platform.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新type为短视频的广告时长


# 更新后查询
for r in db.platform.find():
    print(r)
