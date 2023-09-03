from flask import Flask, render_template, jsonify, request
from handler import dynasty, event
from config import db, data_import
import datetime

app = Flask(__name__)

app.debug = True

with app.app_context():
    data_import()

# 注册蓝图
app.register_blueprint(dynasty.bp)
app.register_blueprint(event.bp)

app.run('127.0.0.1', 8001)
