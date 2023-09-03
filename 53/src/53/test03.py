from data_init import db
from pprint import pprint


# 更新前，打印 name 是小童的文档
pprint(db.student.find_one({'name': '小童'}))
print('='*50)

# 在下方写你的代码:查询歌曲'少年'的id，把他添加到'小童'收藏的歌曲列表中


# 更新后打印小童文档
pprint(db.student.find_one({'name': '小童'}))
