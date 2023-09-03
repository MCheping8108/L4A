from flask import Flask, render_template,request

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/user/register',methods=['GET'])
def regist_page():
	return render_template('test04.html')


@app.route('/user/register',methods=['POST'])
def register():
	username = request.form.get('username')
	
	return username+'，欢迎你！'


# 启动服务器程序
app.run(host='127.0.0.1', port=5000)


