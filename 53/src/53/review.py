import pymongo
from pprint import pprint

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['database53']
db.cartoon.delete_many({})
db.role.delete_many({})
db.cartoon.insert_many(
    [
        {'name': '小猪佩奇', 'type': '动画片'},
        {'name': '熊出没', 'type': '动画片'}
    ]
)
db.role.insert_many(
    [
        {'name': '佩奇', 'description': '是一只非常可爱的小猪，她和她的妈妈、爸爸以及弟弟乔治生活在一起，喜欢跳泥坑，最喜欢吃的是意大利面和巧克力蛋糕。'},
        {'name': '乔治', 'description': '佩奇的弟弟，已经上幼儿园了。性格非常像现实中的小男孩，活泼调皮，喜欢吃意大利面和巧克力蛋糕，喜欢喝果汁，喜欢跳泥坑，最最喜欢的是恐龙。'},
        {'name': '光头强', 'description': '聪明无比，但经常聪明反被聪明误，总想着伐木挣钱'},
    ]
)

if __name__ == '__main__':
    # 在下方你的代码：找到“乔治”和“佩奇”这两个角色，把它们和“小猪佩奇”这部动画片通过引用式建立二者的关系

    pprint(db.cartoon.find_one({'name': '小猪佩奇'}))

