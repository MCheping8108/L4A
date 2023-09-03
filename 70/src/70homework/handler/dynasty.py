from flask import Blueprint, render_template, request, jsonify
from config import db
from bson import ObjectId

bp = Blueprint('dynasty', __name__)


# 首页显示所有朝代，并显示大唐盛世唐朝的历史人物和历史事件
@bp.route('/', methods=['GET'])
def home():
    # 查询所有朝代
    dynasties = list(db.history_dynasty.find())
    # 唐朝是列表中的第11个元素
    tang = dynasties[10]
    # 取出唐朝的所有历史名人
    persons = tang['persons']
    # 取出唐朝的所有历史事件
    event_list = list(
        db.history_event.find({'date': {'$gte': tang['start'], '$lte': tang['end']}}).sort('date', -1))
    return render_template('index.html', dynasties=dynasties, dynasty=tang, persons=persons, event_list=event_list)


# 获取某个朝代信息
@bp.route('/dynasty', methods=['GET'])
def get_dynasty():
    dname = request.args.get('name')
    dynasty = db.history_dynasty.find_one({'name': dname})
    dynasty['_id'] = str(dynasty['_id'])
    return jsonify({'data': dynasty})


# 获取某个朝代下的历史人物
@bp.route('/person', methods=['GET'])
def get_person():
    dname = request.args.get('name')
    dynasty = db.history_dynasty.find_one({'name': dname})
    persons = dynasty['persons']
    for p in persons:
        p['_id'] = str(p['_id'])
    return jsonify({'data': persons})


# 在下方写你的代码：获取某个历史人物信息
@bp.route('/info', methods=['GET'])
def get_info():
    # 获取请求参数人物id并转成ObjectId对象
   
    # 查询对应id的历史人物信息
    
    # 渲染info.html，通过模板变量person返回历史人物信息
    return ''
















