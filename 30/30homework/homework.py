from flask import Flask,render_template,request,jsonify
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)

articles = [
  {'photo':'work01.png','detail':'时报和星期日泰晤士报'},
  {'photo':'work02.png','detail':'丰田Supra'},
  {'photo':'work03.png','detail':'天空营销'},
  {'photo':'work04.png','detail':'不要开车顽皮，开车不错'},
  {'photo':'work05.png','detail':'他的黑暗材料'},
  {'photo':'work06.png','detail':'林地人最想要的'},
  {'photo':'work07.png','detail':'神奇的野兽：格林德瓦的犯罪'},
  {'photo':'work08.png','detail':'Ciclope'},
  {'photo':'work09.png','detail':'Mary Poppins回归'},
  {'photo':'work10.png','detail':'Air New Zealand，Magic Leap'},
  {'photo':'work11.png','detail':'即将上映的电影'},
  {'photo':'work12.png','detail':'MARS 2'}
]

@web.route('/framestore',methods=['GET'])
def framestore():
  return render_template('framestore.html')

@web.route('/articles',methods=['GET'])
def articles_list():
  # 在下方写你的代码：jsonify()
  return jsonify(articles)

web.run(host='127.0.0.1',port=5000)

