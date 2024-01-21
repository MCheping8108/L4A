from flask import Flask, render_template, jsonify, request
from data import data_init
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['movies']

app = Flask(__name__)

app.debug = True

with app.app_context():
    data_init.data_local()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# 票房排行榜
@app.route('/ranking', methods=['GET'])
def get_ranking():
    # 获取票房前10的电影
    movies = list(db.ranking.find()
                  .sort('boxOffice', -1).limit(10))

    # 获取票房在20亿到30亿之间的影片，按票房降序排列，取前10条电影数据
    movies = list(db.ranking.find({'boxOffice': {'$gte': 200000, '$lte': 300000}})
                  .sort('boxOffice', -1).limit(10))

    # 在下方写你的代码：获取票房大于30亿的动作片，并按票房降序排列，取出前10条
    movies = list(db.ranking.find({'boxOffice': {'$gte': 30000000}, 'type': '动作'}).sort('boxOffice', -1).limit(10))

    for d in movies:
        d['_id'] = str(d['_id'])
    return jsonify(movies)


# 高分推荐
@app.route('/score', methods=['GET'])
def get_score():
    # 获取页数page
    page = int(request.args.get('page'))
    # 按豆瓣评分降序排序并分页展示10条文档
    movies = list(db.score.find().sort('rate', -1
                                       ).skip((page - 1) * 10).limit(10))
    for d in movies:
        d['_id'] = str(d['_id'])
    return jsonify(movies)


# 高分推荐总页数
@app.route('/pages', methods=['GET'])
def get_page():
    count = db.score.count_documents({})
    if count % 10 == 0:
        pages = count / 10
    else:
        pages = count // 10 + 1
    return jsonify(pages)


app.run('127.0.0.1', 8000)
