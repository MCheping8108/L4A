from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def my_home():
    return render_template('homework.html')


# 在下方写你的代码：设置404错误处理器


if __name__ == '__main__':
    app.run(port=5000)
