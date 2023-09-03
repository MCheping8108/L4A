from flask import Flask, render_template, request

# 创建Falsk应用
app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'xiaotong', 'password': '123456'},
    {'id': '2', 'username': 'xiaomei', 'password': '000000'},
    {'id': '3', 'username': 'xiaoming', 'password': '888888'}
]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


# @app.route('/user/login_data', methods=['POST'])
# def login2():
#     # 在下方写你的代码：获取用户名和密码
#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = find(username)
#     if user is None:
#         return render_template('login.html', username=username, user_msg='用户名不存在')
#     if user['password'] != password:
#         return render_template('login.html', username=username, pass_msg='密码错误，请重试')
#     return render_template('index.html')


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    # return render_template('login.html')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = find(username)
        if user is None:
            return render_template('login.html', username=username, user_msg='用户名不存在')
        if user['password'] != password:
            return render_template('login.html', username=username, pass_msg='密码错误，请重试')
        return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
