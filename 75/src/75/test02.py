import os
from werkzeug.datastructures import FileStorage
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('test02.html')


@app.route('/test02', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的多个文件filelist
    pass
    # 定义提示信息 data 等于'提示信息：'

    # 遍历接收到的文件列表

        # 获取文件名

        # 获取文件名的扩展名

        # 如果扩展名是'.png'或者是'.jpg'

            # 则读取图片内容

            # 以 wb 模式打开一个新的同名图片

            # 在新的图片中写入原图片内容

            # 关闭文件

            # 定义该文件的说明信息 des 等于'上传成功；'

        # 否则文件类型不符合要求

            # 定义该文件的说明信息 des 等于'文件类型不符合要求；'

        # 在提示信息 data 中累加每个文件的说明信息 des

    return render_template('test02.html', data=data)


if __name__ == '__main__':
    app.run(port=8002)
