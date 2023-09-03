import pymongo, os, json

ip = '127.0.0.1'
port = 27017
database = 'blog'
client = pymongo.MongoClient(ip, port)
db = client['database34']

data_path = './data'


# 导入原始数据的方法
def data_import():
    for maindir, subdir, file_list in os.walk(data_path):
        for file_name in file_list:
            if file_name[file_name.rindex('.'):] == '.json':
                coll = file_name[:file_name.rindex('.')]
                coll_list = db.list_collection_names()
                if coll in coll_list:
                    # 集合已经存在
                    continue
                with open(data_path + '/' + file_name, encoding='utf-8') as file:
                    str = file.read()
                    if str is '' or str is None:
                        continue
                    else:
                        data = []
                        data.extend(json.loads(str))
                        db[coll].insert_many(data)
