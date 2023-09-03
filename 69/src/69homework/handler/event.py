from flask import Blueprint, render_template, request, jsonify
from config import db
import datetime

bp = Blueprint('event', __name__)


# 在下方写你的代码：获取历史事件
@bp.route('/list', methods=['GET'])
def get_list():
    # 获取请求参数朝代名称，并根据名称查询朝代信息

    # 如果朝代开始时间不存在，返回相应信息

    # 查询date大于等于朝代开始时间并小于等于朝代结束时间的文档

    # 把文档中_id转为字符串并格式化时间

    return ''


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
