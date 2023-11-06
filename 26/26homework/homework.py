from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def my_home():
    return render_template('homework.html')


# 在下方写你的代码：设置404错误处理器
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=5000)
