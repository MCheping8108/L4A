import time, pymongo

ip = '127.0.0.1'
port = 27017
database = 'database47'

client = pymongo.MongoClient(ip, port)
db = None


# 获取数据库
def get_db():
    global db
    if not db:
        db = client[database]
    return db


# 读文档+插入到数据库，大约需要10秒钟
def init_db():
    with open('./data/students.txt', 'r', encoding='UTF-8') as f:
        db = get_db()
        if db.student.count_documents({}) > 0:
            print('database47.student已完成初始化，不需要重复操作')
            return

        # 读取数据
        time1 = time.time()
        content = f.read()
        doc_list = eval(content)
        print('读文档时间 ', time.time() - time1)

        time2 = time.time()
        # 写入数据库
        db.student.insert_many(doc_list)
        print('插入到数据库时间 ', time.time() - time2)
        print('database47.student初始化完成！')


# 读文档+插入到数据库，大约需要10秒钟
def init_scores():
    with open('./data/stu_scores.txt', 'r', encoding='UTF-8') as f:
        db = get_db()
        if db.stu_score.count_documents({}) > 0:
            print('database47.stu_score已完成初始化，不需要重复操作')
            return

        # 读取数据
        time1 = time.time()
        content = f.read()
        doc_list = eval(content)
        print('读文档时间 ', time.time() - time1)

        time2 = time.time()
        # 写入数据库
        db.stu_score.insert_many(doc_list)
        print('插入到数据库时间 ', time.time() - time2)
        print('database47.stu_score初始化完成！')
