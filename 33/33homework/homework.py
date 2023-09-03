from config import db


def animal_init():
    a = list(db.animal.find())
    if len(a) > 0:
        return
    animals = [
        {'name': '猫', 'type': '哺乳类'},
        {'name': '狗', 'type': '哺乳类'},
        {'name': '鸡', 'type': '鸟类'},
        {'name': '蛇', 'type': '爬行类'},
        {'name': '青蛙', 'type': '两栖类'},
        {'name': '草鱼', 'type': '鱼类'},
        {'name': '鲸鱼', 'type': '哺乳类'},
        {'name': '鸽子', 'type': '鸟类'},
        {'name': '鳄鱼', 'type': '爬行类'},
        {'name': '蟾蜍', 'type': '两栖类'}
    ]
    db.animal.insert_many(animals)


animal_init()

if __name__ == '__main__':
    # 在下方写你的代码：删除动物集合中的 哺乳类

    # 遍历
    result = db.animal.find()
    for animal in result:
        print(animal)
