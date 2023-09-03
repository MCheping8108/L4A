from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

information = {'version': 'Ver.0.2.94.1', 'file_length': '1.95G', 'update_time': '2019-1-29'}


@web.route('/sdo', methods=['GET'])
def sdo():
    # 在下方写你的代码：返回模板变量
    return render_template('sdo.html')


web.run(host='127.0.0.1', port=8001)
