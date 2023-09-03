from flask import Flask, render_template, request

# 创建Falsk应用
app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'xiaotong', 'password': '123456'},
    {'id': '2', 'username': 'xiaomei', 'password': '000000'},
    {'id': '3', 'username': 'xiaoming', 'password': '888888'},
    {'id': '4', 'username': 'admin', 'password': 'admin'}
]

def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，
        如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None



# 下方完成你的代码：设置访问路径：/user/login
@app.route('/user/login')
def login():
    # 返回首页login.html
    return render_template('login.html')

@app.route('/user/login_data', methods=['GET'])
def login2():
    # 获取请求参数用户名和密码，用变量username和password保存
    username = request.args.get('username')
    password = request.args.get('password')
    # 查找用户是否存在 user = find(username)
    user = find(username)
    print(user)
    return ''
    if user is None:
        return render_template('login.html', username=username ,user_msg='用户名不存在')
    elif user['password'] != password:
        return render_template('login.html', username=username, pass_msg='密码错误')
    else:
        return render_template('index.html')
    # 判断用户名是否存在
    # if user:
    #     # 判断密码是否正确
    #     if user['password'] == password:
    #         return "登录成功"
    #     else:
    #         return "密码错误"
    # else:
    #     return "用户名不存在"

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
app.run(host='127.0.0.1', port=9000)
