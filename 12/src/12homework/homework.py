from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

info = {'message': '现已上市蓝光，DVD和数字', 'title': '铁巨人：签名版'}


@web.route('/giant', methods=['GET'])
def minecraft():
    # 传递模板变量 info
    return render_template('giant.html')


web.run(host='127.0.0.1', port=5000)
