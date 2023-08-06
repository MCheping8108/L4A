from flask import Flask, render_template

# 创建Falsk应用
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


# 请在下方写你的代码
# 游戏页面
# 设置路由
@app.route('/game')
def game():
    # 返回game.html页面
    return render_template('game.html')
# 一站到底页面
# 设置路由/quiz
@app.route('/quiz')
def quiz():
    # 返回quiz.html页面
    return render_template('quiz.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
