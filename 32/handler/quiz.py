from flask import Blueprint, render_template

bp = Blueprint('quiz', __name__)


@bp.route('/quiz')
def game():
	return render_template('quiz.html')
