import pymongo
import datetime


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database63
    db.mail.delete_many({})
    db.mail.insert_many(
        [
            {'receiver': '小童', 'sender': '小美', 'time': datetime.datetime(2020, 8, 25)},
            {'receiver': '小童', 'sender': '小娜', 'time': datetime.datetime(2020, 8, 25)},
            {'receiver': '小童', 'sender': '小涵', 'time': datetime.datetime(2020, 8, 24)},
            {'receiver': '小童', 'sender': '小冰', 'time': datetime.datetime(2020, 8, 26)},
            {'receiver': '小童', 'sender': '佳佳', 'time': datetime.datetime(2020, 8, 26)},
            {'receiver': '小童', 'sender': '小丽', 'time': datetime.datetime(2020, 8, 26)},
        ]
    )

    return db


db = data_init()
