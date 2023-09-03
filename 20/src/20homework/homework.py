from flask import Flask, render_template,request,redirect

# 创建Flask应用
app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
	{'id':'1','username':'xiaotong','password':'123456'},
	{'id':'2','username':'xiaomei','password':'000000'},
	{'id':'3','username':'yunyun','password':'888888'}
]

def find(username):
	'''
		根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
	'''
	for user in users:
		if user['username'] == username:
			return user
	return None

@app.route('/user/login_data', methods=['POST'])
def login2():
	# 请在下方写你的代码：获取用户名和密码
	
	# 查找用户名
	
	# 判断用户名，为None则返回登录页，给出提示信息
	
	# 判断密码，密码错误则返回登录页，给出提示信息
	
	# 判断成功，重定向到首页
	

@app.route('/user/login', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/')
def home():
	return render_template('index.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=5000)
