from flask import Blueprint, render_template, request, jsonify
from config import db

bp = Blueprint('dynasty', __name__)


# 在下方写你的代码：首页显示所有朝代，并显示大唐盛世唐朝的历史人物和历史事件
@bp.route('/', methods=['GET'])
def home():
    # 查询所有朝代

    # 唐朝是列表中的第11个元素

    # 取出唐朝的所有历史名人

    # 取出唐朝的所有历史事件

    return ''


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
