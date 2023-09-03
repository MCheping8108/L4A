import pymongo


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database62
    db.movie.delete_many({})
    db.movie.insert_many(
        [
            {'name': '功夫熊猫', 'role': ['阿宝', '大龙', '美美']},
            {'name': '千与千寻', 'role': ['千寻', '白龙', '汤婆婆', '无脸男']},
            {'name': '龙猫', 'role': 4},

        ]
    )

    return db


db = data_init()
