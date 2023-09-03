import pymongo


def data_init():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.database58
    db.party.delete_many({})
    db.party.insert_many(
        [
            {'name': '武术', 'time': '17:00', 'num': 8},
            {'name': '舞蹈', 'time': '17:30', 'num': 7},
            {'name': '古筝', 'time': '17:50', 'num': 4},
            {'name': '唱歌','num': 2},
            {'name': '唱歌', 'time': '18:15', 'num': 2},
        ]
    )

    return db


db = data_init()
