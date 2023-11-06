from flask import Flask, jsonify, request, render_template
import logging

app = Flask(__name__)
app.debug = True

# 存储报名用户
users = []

# 日志配置
logging.basicConfig(level=logging.DEBUG,
                    # 日志写入文件
                    filename="./test02.log")


@app.route('/')
def index():
    return render_template('test02.html')


@app.route('/test02', methods=['POST'])
def test02():
    # 请在下方写你的代码：获取用户姓名和性别，使用日志logging打印用户信息
    name = request.form.get('name')
    gender = request.form.get('gender')
    logging.info('user:%s, gender:%s' % (name, gender))
    users.append({'name': name, 'gender': gender})

    return render_template('test02.html', data='报名成功')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
