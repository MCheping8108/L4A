import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database48
db.students.delete_many({})
db.students.insert_many(
    [
        {'name': '王湾', 'gender': '男', '语文': 90, '数学': 94},
        {'name': '王美丽', 'gender': '女', '语文': 95, '数学': 84},
        {'name': '李茉莉', 'gender': '女', '语文': 88, '数学': 94},
        {'name': '李井田', 'gender': '男', '语文': 94, '数学': 80},
        {'name': '田甜', 'gender': '女', '语文': 95, '数学': 90},
        {'name': '田海', 'gender': '男', '语文': 70, '数学': 80},
        {'name': '马牛顿', 'gender': '男', '语文': 85, '数学': 88},
        {'name': '孙言', 'gender': '男', '语文': 75, '数学': 88},
        {'name': '钟美美', 'gender': '女', '语文': 95, '数学': 92},
        {'name': '安安', 'gender': '女', '语文': 90, '数学': 90},
        {'name': '牛小乐', 'gender': '女', '语文': 67, '数学': 70},
        {'name': '马天宇', 'gender': '男', '语文': 80, '数学': 99},
        {'name': '史小鹏', 'gender': '男', '语文': 91, '数学': 99},
        {'name': '张暗涵', 'gender': '女', '语文': 88, '数学': 79},
        {'name': '张亮亮', 'gender': '男', '语文': 77, '数学': 70},
        {'name': '朱子涵', 'gender': '女', '语文': 95, '数学': 100},
        {'name': '赵照', 'gender': '女', '语文': 90, '数学': 96},
        {'name': '李子期', 'gender': '男', '语文': 94, '数学': 96},
        {'name': '李木子', 'gender': '女', '语文': 84, '数学': 96},
        {'name': '王子瑞', 'gender': '男', '语文': 98, '数学': 100},

    ]
)

# 在下方写你的代码：统计该班同学男生和女生的数学成绩平均值
