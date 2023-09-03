import os
from werkzeug.datastructures import FileStorage
from flask import Flask, request, render_template

debug = True
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('review.html')


@app.route('/review', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的多个文件filelist

    # 定义提示信息 data 等于'上传成功：'

    # 遍历接收到的 FileStorage 文件对象列表

        # 获取文件名

        # data 累加文件名，多个文件名之间用&nbsp;&nbsp;分割
       
    return render_template('review.html', data=data)


if __name__ == '__main__':
    app.run(port=5001)
