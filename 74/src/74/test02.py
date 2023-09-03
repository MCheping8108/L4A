import os, config
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('test02.html')


@app.route('/upload', methods=['POST'])
def upload():
    data = config.check_form(request)
    # 在下方写你的代码：接收文件pic
    
    # 如果文件不存在，则设置提示信息 data 为“请设置表单enctype的值为multipart/form-data”
  
    # 否则设置提示信息 data 为“某某文件名上传成功”

    return render_template('test02.html', data=data)


if __name__ == '__main__':
    app.run(port=8002)








