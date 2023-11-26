from data_init import db

# 更新前查询
for r in db.platform.find():
    print(r)
print('------------------')

# 在下方写你的代码：更新type为短视频的广告时长
db.platform.update_many({'type': '短视频'}, {'$set': {'ad_time': '999999999s'}})


# 更新后查询
for r in db.platform.find():
    print(r)
