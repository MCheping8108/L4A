from flask import Flask,render_template,request
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/active',methods=['GET'])
def active():
    return render_template('topys_active.html')


@web.route('/chat',methods=['GET'])
def chat():
    return render_template('topys_chat.html')


web.run(host='127.0.0.1',port=8002)
