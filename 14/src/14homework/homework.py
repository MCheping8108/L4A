from flask import Flask,render_template,request


web = Flask(__name__)


@web.route('/qik',methods=['GET'])
def login_page():
  return render_template('7k7k.html')


@web.route('/login',methods=['POST'])
def login():
  # 在下方写你的代码：获取用户名和密码

  return ""


web.run(host='127.0.0.1',port=5000)
