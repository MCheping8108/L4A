from flask import Blueprint, render_template, redirect, request, jsonify, session, make_response
from config import db
from bson import ObjectId

bp = Blueprint('microblog', __name__)


def microblog_find(page, count=5, type='paging'):
	'''
	:param page: 页数
	:param count: 每页显示数量
	:param type: 类型，paging表示分页，init表示从下标0开始
	:return: 根据 page 返回列表 microblogs 中的对象
	'''
	data = None

	if type == 'paging':
		data = list(db.microblog.find().skip((page - 1) * count).limit(count).sort('create_time', -1))
	elif type == 'init':
		data = list(db.microblog.find().limit(page * count).sort('create_time', -1))

	return data


@bp.route('/')
def index():
	# 若没有则重定向到登录页
	if session.get('user') is None:
		return redirect('/user/login')
	user = session['user']

	# 获取Cookie中保存的用户名
	username = request.cookies.get('username', '')

	# 从 cookie 中获取当前页数
	page = request.cookies.get('page')
	if page is None:
		page = 1
	microblog_data = microblog_find(int(page), type='init')
	return render_template('index.html', user=user, microblogs=microblog_data)


@bp.route('/microblog/load', methods=['GET'])
def microblog_load():
	# 从 cookie 中获取当前页数
	page = request.cookies.get('page')
	print(page)
	# page是None，默认加载第2页，否则加载当前页的下一页
	if page is None:
		page = 2
	else:
		page = int(page) + 1
	microblog_data = microblog_find(page)

	# 将 ObjectId 类型值转成字符串
	for blog in microblog_data:
		blog['_id'] = str(blog['_id'])
		blog['author']['_id'] = str(blog['author']['_id'])
	response = make_response(jsonify({'data': microblog_data}))

	if len(microblog_data) > 0:
		# 将当前页数 page 保存到 cookie 中
		response.set_cookie("page", str(page))

	return response


@bp.route('/microblog/detail', methods=['GET'])
def detail():
	# 在下方写你的代码：根据 session 判断用户是否登录，如果没有登录，则重定向到登录页/user/login

	# 获取微博 id

	# 根据微博 id 查询对应微博文档

	return render_template('detail.html')
