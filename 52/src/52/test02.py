from data_init import db
from pprint import pprint

# 在下方写你的代码:找到皮卡丘、杰尼龟对应的文档，


# 构造皮卡丘、杰尼龟的 id 列表
pikachu_id = db.pokemon.find_one({'name': '皮卡丘'})['_id']
squirtle_id = db.pokemon.find_one({'name': '杰尼龟'})['_id']
pokemon_ids = [pikachu_id, squirtle_id]
db.role.update_one({'name': '小智'}, {'$set': {'pokemon': pokemon_ids}})
# 把它们与 小智 建立引用式关系
print(db.pokemon.update_many({'_id': {'$in': pokemon_ids}}, {'$set': {'friend': '小智'}}))


