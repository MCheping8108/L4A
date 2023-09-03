from data_init import db, pencil_box_init

pencil_box_init()

if __name__ == '__main__':
    # 在下方写你的代码：从文具盒中删除钢笔

    # 遍历
    result = db.pencil_box.find()
    for stationery in result:
        print(stationery)
