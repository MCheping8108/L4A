from flask import Flask, render_template, request, Response, jsonify
from datetime import timedelta

comic = [
    {'category': 1, 'image': '01.png', 'title': '吾猫当仙'},
    {'category': 1, 'image': '02.png', 'title': '千穹——小圣江湖'},
    {'category': 1, 'image': '03.png', 'title': '丧尸高手'},
    {'category': 1, 'image': '04.png', 'title': '因为我是开武器店的大叔'},
    {'category': 1, 'image': '05.png', 'title': 'God pupil 驱敌士之眼'},
    {'category': 2, 'image': '06.png', 'title': 'Mocmoc摩丝摩丝'},
    {'category': 2, 'image': '07.png', 'title': 'Hamicat哈咪猫'},
    {'category': 2, 'image': '08.png', 'title': '小巫日记'},
    {'category': 2, 'image': '09.png', 'title': '小明系列漫画'},
    {'category': 2, 'image': '10.png', 'title': '铅笔贱 治愈系手绘'}
]

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/', methods=['GET'])
def dmzj():
    return render_template('home.html')


@web.route('/comic', methods=['GET'])
def cartoon_list():
    # 在下方写你的代码：获取卡通动漫类别category，然后通过预留的comic_find()方法查询出动漫数据

    return


def comic_find(category=None):
    '''
      查询漫画内容的方法
    '''
    c_list = []
    for c in comic:
        if c['category'] == int(category):
            c_list.append(c)
    return c_list


web.run(host='127.0.0.1', port=5000)
