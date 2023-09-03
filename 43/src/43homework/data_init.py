import pymongo, json


def nba_init():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['database43']
    with open('./data/players.json', encoding='utf-8') as p:
        str = p.read()
        j = json.loads(str)
        data_list = j['RECORDS']
        if len(list(db.players.find())) <= 0:
            for data in data_list:
                db.players.insert_one(data)
    return db


db = nba_init()
