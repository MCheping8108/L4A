from flask import Flask, render_template, request
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/storm', methods=['GET'])
def storm():
    return render_template('storm.html')


@web.route('/teach', methods=['GET'])
def teach():
    return '<p>移动 ：将英雄从A点移动至B点应该成为一种习惯。</p><p>技能 ：轻松惬意地使用法术和技能。</p><p>战斗 ：查看生命值、攻击、治疗等等，还要了解什么时候应该进行战略性撤退。</p>'


web.run(host='127.0.0.1', port=8000)
