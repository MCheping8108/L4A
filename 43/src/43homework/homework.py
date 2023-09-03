from data_init import db
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    data = list(
        # 在下方写你代码：在集合 players 中查看猛龙队员的薪资信息，按排名 ranking 升序排列，显示前5名球员


    )
    return render_template('table.html', data=data)


app.run('127.0.0.1', 5000)
