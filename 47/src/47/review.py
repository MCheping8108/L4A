import config, time
from pprint import pprint

# 若没有初始化数据库，则初始化，若已初始化，则什么都不做
config.init_scores()
# 获取数据库
db = config.get_db()

# 在下方写你的代码：统计男生和女生的语文成绩平均值，并打印在控制台
