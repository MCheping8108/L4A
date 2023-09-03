from flask import Blueprint, render_template

# 创建quiz蓝图
bp = Blueprint('quiz', __name__)


@bp.route('/quiz')
def game():
    return render_template('quiz.html')
