from flask import Flask, render_template
from player_init import db

app = Flask(__name__)

app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 在下方写你打代码：查询迈克尔-乔丹的场均得分 score 超过30分的赛季有多少？

    return render_template('table.html', data=data)


app.run(host='127.0.0.1', port=8003)
