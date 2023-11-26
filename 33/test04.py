from data_init import db, garbage_init

# 初始化垃圾数据
garbage_init()

if __name__ == '__main__':
    # 在下方写你的代码：删除有害垃圾
    db.garbage.delete_many({'type': '有害垃圾'})

    # 寻找可回收垃圾
    result = db.garbage.find({'type': '可回收垃圾'})
    for garbage in result:
        print(garbage)


    # 遍历
    # result = db.garbage.find()
    # for garbage in result:
    #     print(garbage)
