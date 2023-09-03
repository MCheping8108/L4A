from flask import Flask, render_template, request

web = Flask(__name__)
web.debug = True

# 已经注册用户的列表
users = [
    {'username': 'xiaotong', 'password': '123456'},
    {'username': 'xiaomei', 'password': '000000'},
    {'username': 'xiaoming', 'password': '888888'}
]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


@web.route('/register', methods=['GET'])
def register_page():
    return render_template('homework.html')


# 请在下方写你的代码
@web.route('/register', methods=['POST'])
def register():
    pass


web.run(host='127.0.0.1', port=5000)
