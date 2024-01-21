from handler import air
from data_init import db
from flask import Flask, render_template, jsonify

app = Flask(__name__)

app.debug = True

app.register_blueprint(air.air)


@app.route("/", methods=['GET'])
def home():
    return render_template('air.html')


@app.route("/PM10", methods=['GET'])
def PM10():
    # 在下方写你的代码：查询PM10大于85的城市
    data = list(db.collection.find({"PM10": {"$gt": 85}}))

    # 预留
    for d in data:
        d['_id'] = str(d['_id'])
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
