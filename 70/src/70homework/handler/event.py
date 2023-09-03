from flask import Blueprint, render_template, request, jsonify
from config import db
import datetime

bp = Blueprint('event', __name__)


# 获取历史事件
@bp.route('/list', methods=['GET'])
def get_list():
    # 获取请求参数朝代名称，并根据名称查询朝代信息
    dname = request.args.get('name')
    dynasty = db.history_dynasty.find_one({'name': dname})
    # 如果朝代开始时间不存在，返回相应信息
    if not dynasty['start']:
        return jsonify({'data': None})
    # 查询date大于等于朝代开始时间并小于等于朝代结束时间的文档
    event_list = list(db.history_event.find
                      ({'date': {'$gte': dynasty['start'],
                                 '$lte': dynasty['end']}}
                       ).sort('date', -1))
    # 把文档中_id转为字符串并格式化时间
    for e in event_list:
        e['_id'] = str(e['_id'])
        e['date'] = e['date'].strftime('%Y-%m-%d')
    return jsonify({'data': event_list})


# 获取‘历史上的今日’
@bp.route('/today', methods=['GET'])
def history_today():
    # 获取日期时间并按照格式拼接为字符串
    now = datetime.datetime.now()
    today = '%s/%s' % (now.month, now.day)
    # 按当前日期查询历史事件并按date升序排序
    event_list = list(db.history_event.find
                      ({'day': today}).sort('date', -1))
    # 格式化时间
    for event in event_list:
        event['date'] = event['date'].strftime('%Y-%m-%d')
    return render_template('event.html',
                           event_list=event_list)


# 查询某月某日的历史事件
@bp.route('/search', methods=['GET'])
def history_search():
    # 获取请求参数月份和日期
    month = request.args.get('month')
    day = request.args.get('day')
    # 根据月份和日期查询历史时间并按date升序排序
    event_list = list(db.history_event.find
                      ({'day': '%s/%s' % (month, day)}).sort('date', -1))
    # 把文档中_id转为字符串并格式化日期
    for event in event_list:
        event['_id'] = str(event['_id'])
        event['date'] = event['date'].strftime('%Y-%m-%d')
    return jsonify({'data': event_list})
