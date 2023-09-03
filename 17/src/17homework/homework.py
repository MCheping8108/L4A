from flask import Flask, render_template, request
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/coc', methods=['GET'])
def coc():
    return render_template('coc.html')


@web.route('/introduce', methods=['GET'])
def introduce():
    return '《部落冲突》是一个战争策略类游戏，在这里你可以提高自己的野蛮人，弓箭手，野猪骑士，皮卡，龙和其他强大的战士与世界各地的玩家对战，提升你的世界排名，与其他玩家联合起来建立强大部落，进行部落对战。'


web.run(host='127.0.0.1', port=5000)
