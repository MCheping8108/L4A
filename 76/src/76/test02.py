from data_init import db
from bson import ObjectId
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('test02.html')


@app.route('/test02', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的文件
    pass
    # 获取文件名
 
    # 读取文件内容
   
    # 如果文件小于 4MB

        # 则在 photos 集合中添加一条文档，内容包括文件名和文件内容

        # 返回响应：渲染 test02.html，提示信息 msg 为：上传成功：+ 文件名
        
    # 如果文件大于 4MB，则返回响应：渲染 test02.html，提示信息 msg 为：文件太大了，请重新选择。


if __name__ == '__main__':
    app.run(port=8002)
