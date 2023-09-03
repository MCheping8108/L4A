import pymongo

ip = '127.0.0.1'
port = 27017
database = 'mall'

client = pymongo.MongoClient(ip, port)
db = None


def get_db():
    global db
    if not db:
        db = client[database]
    return db


db = get_db()
