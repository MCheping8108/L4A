import pymongo, json


def trans_date(s):
    a = s.split('/')
    a.insert(0, a.pop())
    return '-'.join(a)


def calendar_init():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['database38']
    if len(list(db.calendar.find())) <= 0:
        with open('./data/calendar.json', encoding='utf-8') as p:
            print('正在初始化数据，请耐心等待...')
            s = p.read()
            data_list = json.loads(s)
            for data in data_list:
                data['Date'] = trans_date(data['Date'])
                db.calendar.insert_one(data)
    return db


db = calendar_init()
