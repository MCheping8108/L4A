import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database37
db.books.remove({})
db.books.insert_many(
    [
        {"name": "爱丽丝漫游奇境记", "author": "刘易斯·卡罗尔", "country": "英国"},
        {"name": "松鼠斯康帕的晚会", "author": "希瑟·S.布坎南", "country": "英国"},
        {"name": "老鼠玛西脱险", "author": "希瑟·S.布坎南", "country": "英国"},
        {"name": "安徒生童话", "author": "安徒生", "country": "丹麦"},
        {"name": "奇怪的房子", "author": "吉见礼司", "country": "日本"},
        {"name": "秘密花园", "author": "弗朗西丝·霍奇森·伯内特", "country": "英国"},
        {"name": "皮皮鲁传", "author": "郑渊洁", "country": "中国"},
        {"name": "蒂拉的天空", "author": "黑格·托尔文/玛丽·康斯坦·约翰逊", "country": "挪威"},
        {"name": "蓝胡子魔王", "author": "沙尔·贝洛", "country": "法国"},
        {"name": "宝葫芦的秘密", "author": "张天翼", "country": "中国"},
        {"name": "山胡桃小姐", "author": "卡罗林·舍温·贝利", "country": "美国"},
        {"name": "缤纷羽毛", "author": "乔伊·考利", "country": "新西兰"},
        {"name": "中魔的城堡", "author": "伊迪丝·内斯比特", "country": "英国"},
        {"name": "天鹅公主与鹿王子", "author": "田犁", "country": "中国"},
        {"name": "热烘烘的蛋糕", "author": "佐古百美", "country": "日本"},

    ]
)
# 在下方写你的代码：(将第2页的数据打印在控制台即可)
