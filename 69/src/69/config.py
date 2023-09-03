import pymongo,os,json,datetime
from bson import ObjectId

ip = '127.0.0.1'
port = 27017
database = 'history'
data_path = './data'

client = pymongo.MongoClient(ip,port)
db = None
def get_db():
  global db
  if not db:
    db = client[database]
  return db

def parse_data(str):
  dt = str.split(' ')
  day,month,year = dt[0].split('/')
  return datetime.datetime(year=int(year),month=int(month),day=int(day))

def data_import():
  for maindir,subdir,file_list in os.walk(data_path):
    for file_name in file_list:
      if file_name[file_name.rindex('.'):] == '.json':
        coll = file_name[:file_name.rindex('.')]
        coll_list = db.list_collection_names()
        if coll in coll_list:
          continue
        with open(data_path + '/' + file_name,encoding='utf-8') as file:
          str = json.loads(file.read())
          if str is '' or str is None:
            continue
          else:
            data = []
            data.extend(str['RECORDS'])
            for d in data:
              if '_id' in d.keys():
                d['_id'] = ObjectId(d['_id'])
              if 'dynasty_id' in d.keys():
                d['dynasty_id'] = ObjectId(d['dynasty_id'])
              if 'start' in d.keys() and d['start'] is not None:
                print(d['start'])
                d['start'] = parse_data(d['start'])
              if 'end' in d.keys() and d['start'] is not None:
                d['end'] = parse_data(d['end'])
              if 'date' in d.keys():
                d['date'] = parse_data(d['date'])
            db[coll].insert_many(data)

db = get_db()
