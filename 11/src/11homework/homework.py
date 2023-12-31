from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

weapons = [
    {'img': 'weapon01.png', 'name': '反弓', 'type': '黄金版'},
    {'img': 'weapon02.png', 'name': '攀登斧头', 'type': '黄金版'},
    {'img': 'weapon03.png', 'name': 'AB .45', 'type': '黄金版'},
    {'img': 'weapon04.png', 'name': '牧师马克二世', 'type': '黄金版'}
]


@web.route('/tomb', methods=['GET'])
def tomb():
    return render_template('tomb.html')


web.run(host='127.0.0.1', port=5000)
