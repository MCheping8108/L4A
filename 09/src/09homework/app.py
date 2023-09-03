import ssl
from flask import Flask, render_template, request
import tools

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
app.debug = True


@app.route('/star', methods=['GET'])
def star():
	# 获取星座数据
	stars = tools.star_list()
	return render_template('star_home.html', stars=stars)


@app.route('/star/fortune', methods=['GET'])
def star_fortune():
	# 获取选择的星座
	star = request.args.get('star')
	# 获取详细星座运势信息
	star_fortune = tools.star_fortune(star=star)
	# 传递星座运势信息
	return render_template('star_fortune.html', fortune=star_fortune)


# 在下方完成代码：展示生肖首页
@app.route('/', methods=['GET'])
def sx():
	return render_template('sx_home.html')


app.run(host='127.0.0.1', port=9000)
