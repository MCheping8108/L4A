import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database51
db.game.delete_many({})
db.game.insert_many(
    [
        {'name': '安琪拉', 'type': '法师', 'life_value': 3323},
        {'name': '妲己', 'type': '法师', 'life_value': 3229},
        {'name': '阿轲', 'type': '刺客', 'life_value': 3269},
        {'name': '后羿', 'type': '射手', 'life_value': 3182},
        {'name': '关羽', 'type': '战士', 'life_value': 3451},
        {'name': '蔡文姬', 'type': '辅助', 'life_value': 3238},
        {'name': '东皇太一', 'type': '辅助', 'life_value': 3201},
        {'name': '典韦', 'type': '战士', 'life_value': 3434},
        {'name': '伽罗', 'type': '射手', 'life_value': 3173},
        {'name': '廉颇', 'type': '坦克', 'life_value': 3543},
        {'name': '刘邦', 'type': '坦克', 'life_value': 3369},
        {'name': '兰陵王', 'type': '刺客', 'life_value': 3292},
        {'name': '猪八戒', 'type': '坦克', 'life_value': 3149},
        {'name': '盾山', 'type': '辅助', 'life_value': 3361},
        {'name': '米莱迪', 'type': '法师', 'life_value': 3166},
        {'name': '娜可露露', 'type': '刺客', 'life_value': 3239},
        {'name': '张飞', 'type': '坦克', 'life_value': 3450},
        {'name': '元歌', 'type': '刺客', 'life_value': 2637},
        {'name': '太乙真人', 'type': '辅助', 'life_value': 3274},
        {'name': '甄姬', 'type': '法师', 'life_value': 3041},

    ]
)

# 在下方写你的代码：统计game集合中不同职业英雄的平均生命值
data = list(db.game.aggregate([
    {'$group':
         {'_id': '$type',
          'avg_lift': {'$avg': '$life_value'}
          }
     }
]))
print(data)
