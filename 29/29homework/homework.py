from flask import Flask, render_template

app = Flask(__name__)

# 调试模式
app.debug = True


# 设置是否已签到的标记


@app.route('/')
def home():
    return render_template('sign.html')


@app.route('/sign')
def sign():
    # 在此处写代码（如果第一次签到，返回 '恭喜您，签到成功！',再次签到，则返回'请勿重复签到！'）
    pass


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000
    )
