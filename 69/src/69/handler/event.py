from flask import Blueprint, render_template
from config import db
import datetime

bp = Blueprint('event', __name__)


# 在下方写你的代码：获取‘历史上的今日’
@bp.route('/today', methods=['GET'])
def history_today():
    # 获取日期时间并按照格式拼接为字符串

    # 按当前日期查询历史事件并按date降序排序

    # 格式化时间

    return ''

