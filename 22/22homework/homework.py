# https://au.163.com/   劲舞团
from flask import Flask, render_template, request, jsonify

gifts = [
    {'number': '01', 'title': '登录有礼', 'image': 'gift01.png', 'content': '活动期间每日登陆有奖，连续7天登陆即得《我们都要好好的》专属头像框'},
    {'number': '02', 'title': '臻选饰品', 'image': 'gift02.png', 'content': '参与专题活动，即可免费获得《我们都要好好的》限定称号及徽章'},
    {'number': '03', 'title': '同款服饰', 'image': 'gift03.png', 'content': '《我们都要好好的》明星主角同款服饰上线'},
    {'number': '04', 'title': '主题金曲', 'image': 'gift04.png', 'content': '《我们都要好好的》主题曲游戏独播'},
    {'number': '05', 'title': 'WIN杂志', 'image': 'gift05.png',
     'content': '关注“劲舞团手游”官方微信公众号（jwtsy163），获得电视剧第一手爆料及专属周边奖励。'}
]

web = Flask(__name__)

web.debug = True


@web.route('/au', methods=['GET'])
def au():
    return render_template('au.html')


@web.route('/gifts', methods=['GET'])
def au_gift():
    # 在下方写你的代码:移除pass，使用jsonify函数返回数据gifts
    pass


web.run(host='127.0.0.1', port=5001)
