from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('test03.html')


@app.route('/test03', methods=['POST'])
def test03():
    # 在下方写你的代码：接收图片文件 my_file
    pass
    # 如果文件不存在，则设置提示信息 data 为“请设置表单enctype的值为multipart/form-data”

    # 否则设置提示信息 data 为“某某文件名上传成功”

    return render_template('test03.html', data=data)


if __name__ == '__main__':
    app.run(port=8003)









