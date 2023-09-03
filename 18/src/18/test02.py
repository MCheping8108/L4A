from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/bns', methods=['GET'])
def bns():
    return render_template('bns.html')


@web.route('/receive', methods=['GET'])
def receive():
    return '领取成功'


web.run(host='127.0.0.1', port=8002)
