from flask import Flask, render_template, request, jsonify, redirect, session
from random import randint
import time, os

app = Flask(__name__)

app.debug = True

key = os.urandom(24)
app.config['SECRET_KEY'] = key

# 已经注册用户的列表
users = [
    {'name': 'xiaoshan', 'password': '123456', 'photo': '/static/imgs/1.jpg'},
    {'name': 'xiaojing', 'password': '000000', 'photo': '/static/imgs/2.jpg'},
    {'name': 'xiaoqi', 'password': '888888', 'photo': '/static/imgs/3.jpg'}
]


def find(name):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['name'] == name:
            return user
    return None


# 消息列表
msgs = []


@app.route('/register', methods=['GET'])
def chat():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    password = request.form.get('password')
    user = find(name)
    if user is not None:
        return render_template('register.html', msg='该用户已被注册')
    # 随机头像
    photo_index = randint(1, 8)
    photo_url = '/static/imgs/' + str(photo_index) + '.jpg'
    # 注册成功，保存在字典中
    user = {'name': name, 'password': password, 'photo': photo_url}
    users.append(user)
    # 注册成功，重定向到登录页
    return redirect('/login')


@app.route('/login', methods=['GET'])
def user_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    user = find(name)
    if user is None:
        return render_template('login.html', user_msg='用户名不存在')
    elif user['password'] != password:
        return render_template('login.html', pass_msg='密码错误，请重试')
    else:
        session['user'] = user
        return redirect('/chat')


@app.route('/chat', methods=['GET'])
def chat_group():
    user = session.get('user')
    if user:
        # 管理员消息，对新用户的欢迎语，将其加入消息列表 msgs
        send_time = int(time.time())
        msg = {'name': 'admin', 'text': '欢迎 <b>' + user['name'] + '</b> 进入聊天室', 'time': send_time}
        msgs.append(msg)
        # 返回用户信息
        photo = user['photo']
        return render_template('chat.html', name=user['name'], photo=photo, time=send_time)
    else:
        return redirect('/login')


@app.route('/group', methods=['POST'])
def receive_msg():
    # 获取传递的值
    name = request.form.get('name')
    photo = request.form.get('photo')
    text = request.form.get('text')
    # 生成接收时间
    receive_time = int(time.time())

    # 打印
    print('%s %s %s %d' % (name, photo, text, receive_time))

    # 构建消息对象
    msg = {'name': name, 'text': text, 'photo': photo, 'time': receive_time}
    # 添加到消息列表
    msgs.append(msg)

    # 返回响应
    return jsonify({'state': 'success', 'time': receive_time})


# 在下方写你的代码：设置get_list路由


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
