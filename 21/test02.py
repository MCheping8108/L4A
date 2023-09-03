from flask import Flask, render_template, request

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/game/info', methods=['GET'])
def register_page():
    return render_template('test02.html')


@app.route('/game/info', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    telephone = request.form.get('telephone')
    return '欢迎  ' + username + '进入梦幻遨游的世界！'


# 启动服务器程序
app.run(host='127.0.0.1', port=8002)
