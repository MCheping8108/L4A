from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

data = [
    {'type': '[新闻]', 'title': '四月桃花季美妆上心，予你十里春光！'},
    {'type': '[新闻]', 'title': '五周年cosplay大赛正式开启，等你!'},
    {'type': '[活动]', 'title': 'welcome，四海珍奇回馈活动正式开启！'},
    {'type': '[新闻]', 'title': '全新天地风云联赛来袭，come on！'},
    {'type': '[活动]', 'title': '燕回初春，天刀四月福利活动大放送！'},
]


@web.route('/tymyd', methods=['GET'])
def tymyd():
    return render_template('tymyd.html', data=data)


web.run(host='127.0.0.1', port=8000)
