import pymongo


def data_init():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['database42']
    d = list(db.sound.find())
    if len(d) <= 0:
        data = [
            {'name': 'Raven H', 'price': '1699', 'company': '百度'},
            {'name': '天猫精灵', 'price': '499', 'company': '阿里巴巴'},
            {'name': '腾讯听听', 'price': '699', 'company': '腾讯'},
            {'name': '叮咚play', 'price': '1899', 'company': '京东'},
            {'name': 'Tichome', 'price': '699', 'company': '出门问问'},
            {'name': '小爱同学', 'price': '299', 'company': '小米'}
        ]
        db.sound.insert_many(data)
    return db


db = data_init()

if __name__ == '__main__':
    # 在下方写你的代码：查询出sound集合中一共有多少个音响

    pass
