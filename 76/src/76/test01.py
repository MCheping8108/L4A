import os
import random
import datetime
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('test01.html')


@app.route('/test01', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的文件

    # 获取文件名

    # 获取文件名的扩展名

    # 获取此时此刻时间戳的总微秒数（要求是整数）

    # 获取 10000-99999 随机整数

    # 创建唯一文件名

    # 在 ./static/images/upload/ 目录下创建指定文件名的文件

    # 读取上传的文件内容并写入到新文件中

    # 关闭文件

    # 创建提示信息：上传成功 + 原文件名

    return render_template('test01.html', data=data)


if __name__ == '__main__':
    app.run(port=8001)
