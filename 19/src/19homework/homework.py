from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

bag_info = [
    {'img': 'bag1.png', 'name': '小挂包', 'type': '单肩包'},
    {'img': 'bag2.png', 'name': '学生包', 'type': '双肩包'},
    {'img': 'bag3.png', 'name': '钱包', 'type': '手拿包'},
    {'img': 'bag4.png', 'name': '通勤包', 'type': '手提包'}
]


@web.route('/bags', methods=['GET'])
def bags():
    # 在下方写你的代码：传递模板变量给前端模板文件
    return render_template('bags.html',)


web.run(host='127.0.0.1', port=5000)
