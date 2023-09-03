from flask import Flask, render_template, request, redirect, jsonify, session

# 创建Flask应用
app = Flask(__name__)
app.debug = True
app.secret_key = '123456'

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'xiaotong', 'password': '123456'},
    {'id': '2', 'username': 'xiaomei', 'password': '000000'},
    {'id': '3', 'username': 'xiaoming', 'password': '888888'}
]

microblogs = [
    {'id': '1', 'username': '小辛辛', 'head': 'head01.jpg', 'photo': 'blog01.png', 'create_time': '2018/12/26'},
    {'id': '2', 'username': 'YUTAR', 'head': 'head02.jpg', 'photo': 'blog02.png', 'create_time': '2018/12/26'},
    {'id': '3', 'username': '赤道', 'head': 'head03.jpg', 'photo': 'blog03.png', 'create_time': '2018/12/26'},
    {'id': '4', 'username': 'Wang Ming', 'head': 'head04.jpg', 'photo': 'blog04.png', 'create_time': '2018/12/26'},
    {'id': '5', 'username': '--中梁--', 'head': 'head05.jpg', 'photo': 'blog05.png', 'create_time': '2018/12/25'},
    {'id': '6', 'username': 'Y-Y', 'head': 'head06.jpg', 'photo': 'blog06.png', 'create_time': '2018/12/25'},
    {'id': '7', 'username': '蘑菇一号', 'head': 'head07.jpg', 'photo': 'blog07.png', 'create_time': '2018/12/25'},
    {'id': '8', 'username': '雇佣兵', 'head': 'head08.jpg', 'photo': 'blog08.png', 'create_time': '2018/12/24'},
    {'id': '9', 'username': '不万能的喜剧', 'head': 'head09.jpg', 'photo': 'blog09.png', 'create_time': '2018/12/24'},
    {'id': '10', 'username': '达达@达', 'head': 'head10.jpg', 'photo': 'blog10.png', 'create_time': '2018/12/24'},
    {'id': '11', 'username': '@@ @@', 'head': 'head11.jpg', 'photo': 'blog11.jpg', 'create_time': '2018/12/23'},
    {'id': '12', 'username': 'Pansy。', 'head': 'head12.jpg', 'photo': 'blog12.jpg', 'create_time': '2018/12/23'},
    {'id': '13', 'username': 'hope', 'head': 'head13.jpg', 'photo': 'blog13.jpg', 'create_time': '2018/12/23'},
    {'id': '14', 'username': '大阿佳@.', 'head': 'head14.jpg', 'photo': 'blog14.jpg', 'create_time': '2018/12/22'},
    {'id': '15', 'username': 'T_T', 'head': 'head15.jpg', 'photo': 'blog15.jpg', 'create_time': '2018/12/22'},
    {'id': '16', 'username': '带牙套的猴子', 'head': 'head16.jpg', 'photo': 'blog16.jpg', 'create_time': '2018/12/22'},
    {'id': '17', 'username': 'DS.大好人๛ก', 'head': 'head17.jpg', 'photo': 'blog17.jpg', 'create_time': '2018/12/21'},
    {'id': '18', 'username': '跌跌荡荡的青春', 'head': 'head18.jpg', 'photo': 'blog18.jpg', 'create_time': '2018/12/21'},
    {'id': '19', 'username': 'sophia', 'head': 'head19.jpg', 'photo': 'blog19.jpg', 'create_time': '2018/12/21'},
    {'id': '20', 'username': 'KKKL', 'head': 'head20.jpg', 'photo': 'blog20.png', 'create_time': '2018/12/21'}
]


def microblog_find(page, count=5, type='paging'):
    '''
    :param page: 页数
    :param count: 每页显示数量
    :param type: 类型，paging表示分页，all表示获取所有，从下标0开始
    :return: 根据 page 返回列表 microblogs 中的对象
    '''

    if type == 'paging':
        start = (page - 1) * count
    elif type == 'init':
        start = 0

    end = page * count

    if start > len(microblogs):
        # 没有更多，返回空列表
        return []

    return microblogs[start:end]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 获取Cookie中保存的上次登录的用户名
        username = request.cookies.get('username', '')

        # 在下方写你的代码：获取session,如果存在，则重定向到首页


        return render_template('login.html', username=username)
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = find(username)
        if user is None:
            return render_template('login.html', username=username, user_msg='用户名不存在')
        if user['password'] != password:
            return render_template('login.html', username=username, pass_msg='密码错误，请重试')

        # 在下方写你的代码：登录成功后，把用户信息存储到session中


        # 获取redirect函数返回的Response对象
        response = redirect('/')
        # 将用户名保存在Cookie中
        response.set_cookie('username', username, max_age=600)

        # 登录成功，重定向到首页
        return response


@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 获取提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断用户名是否已存在
        user = find(username)
        if user is not None:
            return jsonify({'status': 'failure', 'msg': '该用户名已被注册'})

        # 注册成功，保存在字典中
        user = {'id': len(users) + 1, 'username': username, 'password': password}
        users.append(user)

        # 注册成功，重定向到登录页
        return jsonify({'status': 'success', 'msg': '恭喜注册成功'})


@app.route('/')
def index():
    # 在下方写你的代码:获取session，如果session不存在，则重定向到登录页


    # 获取Cookie中保存的用户名
    username = request.cookies.get('username', '')
    # 从 cookie 中获取当前页数
    page = request.cookies.get('page')
    if page is None:
        page = 1
    microblog_data = microblog_find(int(page), type='init')

    return render_template('index.html', username=username, microblogs=microblog_data)


@app.route('/microblog/load', methods=['GET'])
def microblog_load():
    # 从 cookie 中获取当前页数
    page = request.cookies.get('page')
    # page是None，默认加载第2页，否则加载当前页的下一页
    if page is None:
        page = 2
    else:
        page = int(page) + 1
    # 通过page获取加载的微博数据
    microblog_data = microblog_find(page)
    response = jsonify({'data': microblog_data})
    if len(microblog_data) > 0:
        # 将当前页数 page 保存到 cookie 中
        response.set_cookie("page", str(page))

    return response


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
