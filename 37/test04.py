from flask import Flask, render_template
from data_init import db

web = Flask(__name__)
web.debug = True


@web.route('/data', methods=['GET'])
def show_data():
    # 在下方写你的代码：查询火影忍者中，性别为女，年龄为13的人物

    return render_template('table.html', data=data)


web.run(host='127.0.0.1', port=8004)
