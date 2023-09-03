from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/index', methods=['GET'])
def home():
    return render_template('test01.html')


web.run(host='127.0.0.1', port=8001)
