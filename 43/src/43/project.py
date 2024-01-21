from flask import Flask, render_template
from data_init import db

app = Flask(__name__)
app.debug = True


@app.route('/store', methods=['GET'])
def app_store():
    # 在下方写你的代码：精品,在渠道小米中按排名升序排列后类别取12条
    data = list(db.apps.find({'channel': '小米'}).sort('ranking', 1).limit(12))

    # 热门，渠道小米中按昨日下载量降序排列，取前12条
    quality_goods = list(db.apps.find({'channel': '小米'}).sort('lastDayDownloadNum', -1).limit(12))

    return render_template('project.html', quality_goods=quality_goods, hots=data)


app.run(host='127.0.0.1', port=8000)
