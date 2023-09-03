from flask import Flask, render_template
from data_init import db

web = Flask(__name__)
web.debug = True


@web.route('/data', methods=['GET'])
def show_data():
    # 请在下方写你的代码：使用逻辑或查询生肖为鼠或者兔的文档

    return render_template('table.html', data=data)


web.run('127.0.0.1', 8003)
