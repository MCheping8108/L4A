from flask import Flask, render_template, request, jsonify
from cal import db

app = Flask(__name__)

app.debug = True


@app.route('/cal', methods=['GET'])
def calendar():
    return render_template('cal.html')


@app.route('/date', methods=['GET'])
def get_date():
    today = request.args.get('today')
    tomorrow = request.args.get('tomorrow')
    # 请在下方写你的代码：使用逻辑或查询今天明天的数据
    
    
    for d in data:
        d['_id'] = str(d['_id'])
    return jsonify(data)


app.run('127.0.0.1', 8000)
