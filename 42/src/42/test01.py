﻿from flask import Flask, render_template
from player_init import db

app = Flask(__name__)

app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 数据查看
    data = list(db.players.find())

    # 在下方写你的代码：统计 科比-布莱恩特 总参赛场次

    # 在下方写你的代码：统计 迈克尔-乔丹 总参赛场次

    return render_template('table.html', data=data)


app.run(host='127.0.0.1', port=8001)
