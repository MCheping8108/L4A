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

    return render_template('detail.html', blog=blog)


# 点赞
@bp.route('/like/create', methods=['GET'])
def like_on():
    # 因为访问该路由的是ajax请求，所以重定向是无效的,故返回json数据让浏览器端完成访问登录页面的操作
    if not session.get('user'):
        return jsonify({'status': 'failure', 'data': '请先登录'})
    # 在下方写你的代码：从 session 中获取用户信息 user

    # 从用户信息中取出用户 id，并转成 ObjectId 对象

    # 获取请求参数微博 id，并转成 ObjectId 对象

    # 更新微博文档，添加点赞者 id（即此时登录用户的 id）

    # 使用 jsonify 返回状态 status 为 success，data为'点赞成功'


# 取消点赞
@bp.route('/like/delete', methods=['GET'])
def like_cancle():
    # 因为访问该路由的是ajax请求，所以重定向是无效的,故返回json数据让浏览器端完成访问登录页面的操作
    if not session.get('user'):
        return jsonify({'status': 'failure', 'data': '请先登录'})
    # 从 session 中获取用户信息 user
    user = session['user']
    # 从用户信息中取出用户 id，并转成 ObjectId 对象
    user_id = ObjectId(user['_id'])
    # 获取请求参数微博 id，并转成 ObjectId 对象
    blog_id = ObjectId(request.args.get('blog_id'))
    # 在下方写你的代码：更新微博文档，删除点赞者 id（即此时登录用户的 id）
    
    # 使用 jsonify 返回状态 status 为 success，data为'取消点赞成功'
    return jsonify({'status': 'success', 'data': '取消点赞成功'})
