from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('homework.html')


@app.route('/homework', methods=['POST'])
def homework():
    # 接收文件 homework_file
    pass
    # 如果文件不存在，则设置提示信息data为“请设置表单enctype的值为multipart/form-data”

    # 否则设置提示信息data为“某文件名上传成功”

    # 渲染 homework.html，返回提示信息 data


if __name__ == '__main__':
    app.run(port=8010)
