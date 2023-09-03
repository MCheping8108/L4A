import pymongo,os,json
from bson import ObjectId
from urllib import request

ip = '127.0.0.1'
port = 27017
database = 'music'

client = pymongo.MongoClient(ip,port)
db = None
def get_db():
  global db
  if not db:
    db = client[database]
  return db

db = get_db()

data_path = './data'

# 导入原始数据的方法
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
              if 'songs_id' in d.keys():
                for i in range(len(d['songs_id'])-1,-1,-1):
                  sid = d['songs_id'][i]
                  d['songs_id'].append(ObjectId(sid))
                  d['songs_id'].remove(sid)
              if 'ranking_list' in d.keys():
                ranking_list = d['ranking_list']
                for rl in ranking_list:
                  rl['_id'] = ObjectId(rl['_id'])
            db[coll].insert_many(data)

def get_music_url(url):
  return request.urlopen(url).read().decode('utf-8')

data_import()
