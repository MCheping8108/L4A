from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('review.html')


@app.route('/review', methods=['POST'])
def review():
    # 下方写你的代码：接收前端传递的文件file

    # 打印文件名

    return render_template('review.html', data='上传成功')


if __name__ == '__main__':
    app.run(port=8000)
