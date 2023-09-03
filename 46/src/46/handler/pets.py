import math
from data_init import db
from flask import Blueprint, render_template, jsonify

pets = Blueprint('pets', __name__)


@pets.route('/')
def home():
    return render_template('pets.html')


@pets.route('/getPages')
def getPages():
    counts = db.pets.find({}).count()
    pages = math.ceil(counts / 6)
    return jsonify({'pages': pages, 'counts': counts})
