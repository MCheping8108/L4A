from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

informations = [
    {'photo': 'info01.png', 'title': '柏言映画携手小米主题 进一步丰富MIUI内容生态 手机厂商第一家！', 'content': '小米主题和柏言映画达成合作将推专属定制主题'},
    {'photo': 'info02.png', 'title': '央视为原创国漫点赞！少年锦衣卫勇夺新光奖最佳新锐动漫奖',
     'content': '2017年9月16日，“新光奖”中国西安第六届国际原创动漫大赛隆重举行。柏言映画原创3D动画《少年锦衣卫》勇夺新光奖最佳新锐动漫奖。'},
    {'photo': 'info03.jpg', 'title': '《少年锦衣卫》第二季定档！', 'content': '《少年锦衣卫》第二季定档9月28日。'},
    {'photo': 'info04.png', 'title': '柏言映画《少年锦衣卫》获2017金龙奖最佳系列动画金奖',
     'content': '《少年锦衣卫》荣获第14届中国动漫金龙奖，成为2017年原创国产动画的双冠王。'},
]


@web.route('/sj', methods=['GET'])
def sj():
    # 在下方写你的代码：传递模板变量
    return render_template('sj.html',)


web.run(host='127.0.0.1', port=8002)
