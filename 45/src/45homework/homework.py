import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database45
db.pictures.delete_many({})
db.pictures.insert_many(
    [
        {"name": "老虎头像", "tags": "简笔画；老虎；彩色；动物"},
        {"name": "大灰熊", "tags": "水彩画；熊；；动物"},
        {"name": "喜鹊", "tags": "简笔画；鸟类；彩色；动物；翅膀"},
        {"name": "杨桃", "tags": "蜡笔画；水果；彩色；植物"},
        {"name": "苹果", "tags": "素描；水果"},
        {"name": "小汽车", "tags": "简笔画；交通工具；彩色"},
        {"name": "老鼠", "tags": "素描；动物"},
        {"name": "佩奇", "tags": "水彩画；卡通；彩色"},
        {"name": "飞机", "tags": "水彩画；交通工具；彩色；翅膀"},
        {"name": "花朵", "tags": "水彩画；植物；彩色；美丽"}

    ]
)
# 在下方写你的代码：找到标签tags包含‘水彩画’的所有文档并在控制台打印
