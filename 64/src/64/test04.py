import calendar
from flask import Flask, render_template

app = Flask(__name__)
# 注册蓝图
app.debug = True


@app.route('/calendar')
def get_calendar():
    # 在下方写你的代码：获取2021年的HTML日历

    return render_template('test04.html', data=data)


if __name__ == '__main__':
    app.run('127.0.0.1', 8001)
