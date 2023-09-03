from data_init import *

db = create_farm()

if __name__ == '__main__':
    # 在下方写你的代码：更新绵羊的数量

    for farm in db.myFarm.find():
        print(farm)
