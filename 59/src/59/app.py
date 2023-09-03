from flask import Flask, render_template, request, jsonify
from config import db, data_import
from bson import ObjectId
from handler import ranking, playlist

app = Flask(__name__)

app.debug = True

with app.app_context():
    data_import()

app.register_blueprint(ranking.ranking)
app.register_blueprint(playlist.playlist)

app.run('127.0.0.1', 8000)
