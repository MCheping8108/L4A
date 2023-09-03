from flask import Flask, request, render_template

debug = True
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homework.html')


@app.route('/homework', methods=['POST'])
def upload():
    # 在下方写你的代码：接收前端发送的多个文件filelist

    # 定义提示信息 data 等于“上传成功”

    # 遍历接收到的文件列表

        # 在提示信息中累加文件名信息

    return render_template('homework.html', data=data)


if __name__ == '__main__':
    app.run(port=5000)
    
    
    
    
    
    
    
