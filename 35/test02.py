from flask import Flask, render_template, request, Response, jsonify
from datetime import timedelta

cartoons = [
    {'type': 1, 'image': '01.jpg', 'title': '【航海王】尾田荣一郎'},
    {'type': 1, 'image': '02.jpg', 'title': '【食戟之灵】附田祐斗'},
    {'type': 1, 'image': '03.jpg', 'title': '【境界触发者】苇原大介'},
    {'type': 2, 'image': '04.jpg', 'title': '【火影忍者】岸本齐史'},
    {'type': 2, 'image': '05.jpg', 'title': '【花样男子】神尾叶子'},
    {'type': 2, 'image': '06.jpg', 'title': '【龙珠】鸟山明'}
]

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/', methods=['GET'])
def manhua():
    return render_template('manhua.html')


@web.route('/list', methods=['GET'])
def manhua_list():
    # 在下方写你的代码：获取漫画类型 type，然后通过预留的cartoon_find()f方法，传入type，查询出漫画数据
   return

                
def cartoon_find(type=None):
    '''
      查询漫画内容的方法
    '''
    c_list = []
    for c in cartoons:
        if c['type'] == int(type):
            c_list.append(c)
    return c_list


web.run(host='127.0.0.1', port=8002)
