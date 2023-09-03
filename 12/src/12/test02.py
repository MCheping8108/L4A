from flask import Flask, render_template
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

hot = {'date': None, 'title': '新赛季起航！世界冠军引爆揭幕战',
       'content': '4个月的等待，战斗的号角再次响彻竞技场！2020CRL春季赛将正式归来，重装升级之后的八支战队，将为捍卫CN最强赛区的荣耀再次出发！nova、gen.g、newbee和x-quest将引爆揭幕战！'}


@web.route('/clash', methods=['GET'])
def clash():
    # 在下方写你的代码：传递模板变量 
    return render_template('clash.html', hot=hot)


web.run(host='127.0.0.1', port=8002)
