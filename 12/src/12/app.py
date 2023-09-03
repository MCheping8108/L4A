from flask import Flask
from handler import user, microblog, quiz, game
from datetime import timedelta

app = Flask(__name__)

app.debug = True
app.send_file_max_age_default = timedelta(seconds=1)

# 注册蓝图
app.register_blueprint(user.user)
app.register_blueprint(microblog.microblog)
app.register_blueprint(quiz.quiz)
app.register_blueprint(game.game)

app.run(host='127.0.0.1', port=8000)
