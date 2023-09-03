from data_init import db
from pprint import pprint


# 更新前，打印 name 是小美的文档
pprint(db.customer.find_one({'name': '小美'}))
print('='*50)

# 在下方写你的代码:查询商品'coke'的id，把他添加到'小美'的商品 id 列表中


# 更新后打印小美文档
pprint(db.customer.find_one({'name': '小美'}))
