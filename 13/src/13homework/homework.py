from flask import Flask, render_template, request

# 创建Flask应用
app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'liangliang', 'password': '123456'},
    {'id': '2', 'username': 'jiangjiang', 'password': '000000'},
    {'id': '3', 'username': 'yunyun', 'password': '888888'}
]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


@app.route('/user/login_data', methods=['GET'])
def login2():
    # 获取请求参数用户名和密码，用变量username和password保存

    # 查找用户是否存在 user = find(username)

    # 判断用户名是否存在

    # 判断密码是否正确

    # 返回“登录成功”
    return " "


@app.route('/user/login', methods=['GET'])
def login():
    # 返回首页mycode.html
    return ""


# 启动服务器程序
app.run(host='127.0.0.1', port=5000)
