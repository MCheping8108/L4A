from flask import render_template, Blueprint
# 请在下方写你的代码：创建store蓝图
bp = Blueprint('store', __name__)
@bp.route('/wm/store')
def wm_store():
    return render_template('store.html')
