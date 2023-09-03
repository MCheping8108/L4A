from flask import Flask
from handler import dynasty, event
from config import data_import


app = Flask(__name__)

app.debug = True

with app.app_context():
    data_import()

# 注册蓝图
app.register_blueprint(dynasty.bp)
app.register_blueprint(event.bp)

app.run('127.0.0.1', 8001)
