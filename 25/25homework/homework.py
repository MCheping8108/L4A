from flask import Flask, render_template, request,redirect
import os
from flask import session

app = Flask(__name__)

# 调试模式
app.debug = True

app.secret_key = '123456'

# 消息列表
msgs = []


@app.route('/')
def index():
    user = None
    if 'user' in session:
        user = session['user']
    return render_template('index.html', user=user)


# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 在下方写你的代码：如果已经登录过，跳转到首页，否则返回登录页
        if 'user' in session:
            return redirect('/')
        return render_template('login.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')
        user = {'name': name, 'pwd': pwd}
        # 在下方写你的代码：登录成功，使用session存储用户名和密码，并且传递用户名给index.html
        session['user'] = user
        return redirect('/')
        return render_template('index.html',user='')


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5004
    )
