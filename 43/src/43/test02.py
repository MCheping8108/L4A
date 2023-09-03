import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.database43
db.music.remove({})
db.music.insert_many(
    [
        {"name": "大象拔河", "singer": "宝宝巴士", "play": 208536, "download": 148536},
        {"name": "蓝精灵", "singer": "群星", "play": 308536, "download": 248532},
        {"name": "奇迹再现", "singer": "毛毛", "play": 288536, "download": 168532},
        {"name": "黑猫警长", "singer": "沈小岑", "play": 508536, "download": 288594},
        {"name": "大头儿子小头爸爸", "singer": "群星", "play": 708536, "download": 149336},
        {"name": "小英雄哪吒", "singer": "孙楠", "play": 608536, "download": 248931},
        {"name": "猪猪侠", "singer": "陈洁丽", "play": 900536, "download": 458599},
        {"name": "围棋少年", "singer": "姜必群", "play": 509536, "download": 168536},
        {"name": "巴啦啦小魔仙", "singer": '大小ann', "play": 448536, "download": 448432},
        {"name": "葫芦金刚", "singer": "王迟", "play": 578536, "download": 348530}
    ]
)
# 在下方写你的代码：数据库中有音乐集合 music，根据歌曲播放量play降序排列并打印在控制台上。


