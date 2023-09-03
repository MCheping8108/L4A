from flask import Flask, render_template, request, redirect

web = Flask(__name__)

web.debug = True


@web.route('/', methods=['GET'])
def home():
    auto_login = request.cookies.get('auto_login')
    if auto_login != 'yes':
        return redirect('/login')
    return render_template('home.html')


@web.route('/login', methods=['GET'])
def login_page():
    # 在下方写你的代码：获取cookie，判断cookie是否为yes
    
    
    return render_template('login.html')


@web.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'xiaotong' and password == '123456':
        response = redirect('/')
        # 在下方写你的代码：设置cookie,键是auto_login, 值是yes
        
    
        return response
    else:
        return '请使用用户名xiaotong，密码123456登录'
    

web.run(host='127.0.0.1', port=5002)
