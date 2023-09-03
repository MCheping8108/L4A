from flask import Flask, render_template, request
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/', methods=['GET'])
def callduty():
    return render_template('callduty.html')


@web.route('/map', methods=['GET'])
def map():
    return '来自于使命召唤现代战争3经典地图，中型地图，坐落于战区山地上的前方作战基地。战场的环境风格和山地陡峭的地形适合突击步枪与冲锋枪的攻防，同时又有多个的视野开阔的火力点适合长距离作战。'


web.run(host='127.0.0.1', port=5000)
