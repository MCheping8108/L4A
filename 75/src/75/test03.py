from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('test03.html')


@app.route('/test03', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的多个文件filelist
    pass
    # 定义提示信息 data 等于'提示信息：'

    # 遍历接收到的文件列表

        # 读取文件内容

        # 获取文件大小

        # 如果文件小于5MB，则在提示信息 data 中累加说明文字'某文件名上传成功'

        # 否则在提示信息 data 中累加说明文字'某文件太大了，请重新选择功'

    return render_template('test03.html', data=data)


if __name__ == '__main__':
    app.run(port=8003)
