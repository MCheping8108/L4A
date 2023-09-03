from flask import Flask,render_template

web = Flask(__name__)
web.debug=True

inform = '【游戏】随时开始工作细胞分娩~'
# inform = None

@web.route('/cells')
def cells():
  return render_template('cells.html',inform=inform)

web.run(host='127.0.0.1',port=5000)
