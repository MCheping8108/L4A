from flask import Blueprint, render_template, redirect, request, jsonify, session, make_response
from config import db
from bson import ObjectId
import datetime

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

    print(microblog_data)

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
        if 'liker_id' in blog:
            for liker_id in blog['liker_id']:
                blog['liker_id'] = str(liker_id)
    print('more...')
    print(microblog_data)

    response = make_response(jsonify({'data': microblog_data}))

    if len(microblog_data) > 0:
        # 将当前页数 page 保存到 cookie 中
        response.set_cookie("page", str(page))

    return response


@bp.route('/microblog/detail', methods=['GET'])
def detail():
    if not session.get('user'):
        return redirect('/user/login')
    blog_id = ObjectId(request.args.get('id'))
    blog = db.microblog.find_one({'_id': blog_id})

    # 是否已经点赞
    user = session['user']
    user_id = ObjectId(user['_id'])
    if 'liker_id' in blog and user_id in blog['liker_id']:
        is_liked = True
    else:
        is_liked = False
    blog['is_liked'] = is_liked
    # 点赞数
    if 'liker_id' in blog:
        blog['likes'] = len(blog['liker_id'])
    else:
        blog['likes'] = 0

    # 评论
    com_list = list(db.comment.find({'blog_id': blog_id}))
    blog['comments'] = len(com_list)
    blog['com_list'] = com_list

    return render_template('detail.html', blog=blog)


# 点赞
@bp.route('/like/create', methods=['GET'])
def like_on():
    # 因为访问该路由的是ajax请求，所以重定向是无效的,故返回json数据让浏览器端完成访问登录页面的操作
    if not session.get('user'):
        return jsonify({'status': 'failure', 'data': '请先登录'})
    user = session['user']
    user_id = ObjectId(user['_id'])
    blog_id = ObjectId(request.args.get('blog_id'))
    db.microblog.update({'_id': blog_id}, {'$push': {'liker_id': user_id}})
    return jsonify({'status': 'success', 'data': '点赞成功'})


# 取消点赞
@bp.route('/like/delete', methods=['GET'])
def like_cancle():
    if not session.get('user'):
        return jsonify({'status': 'failure', 'data': '请先登录'})
    user = session['user']
    user_id = ObjectId(user['_id'])
    blog_id = ObjectId(request.args.get('blog_id'))
    db.microblog.update({'_id': blog_id}, {'$pull': {'liker_id': user_id}})
    return jsonify({'status': 'success', 'data': '取消点赞成功'})


@bp.route('/comments/list', methods=['GET'])
def comment_list():
    blog_id = ObjectId(request.args.get('blog_id'))
    com_list = list(db.comment.find({'blog_id': blog_id}))
    # 将ObjectId类型转成str
    for comment in com_list:
        comment['_id'] = str(comment['_id'])
        comment['blog_id'] = str(comment['blog_id'])
        comment['author']['_id'] = str(comment['author']['_id'])
    return jsonify({'status': 'success', 'data': com_list})


@bp.route('/comments/create', methods=['POST'])
def comment():
    if not session.get('user'):
        return jsonify({'status': 'failure', 'data': '请先登录'})

    user = session['user']
    user_id = ObjectId(user['_id'])
    blog_id = ObjectId(request.form.get('blog_id'))
    content = request.form.get('content')
    # 保存评论
    user = db.user.find_one({'_id': user_id})
    comment = {
        'author': user,
        'blog_id': blog_id,
        'content': content,
        'create_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    db.comment.insert_one(comment)
    return jsonify({'status': 'success', 'data': '评论成功'})
