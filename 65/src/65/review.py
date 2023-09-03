import calendar
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/calendar')
def get_calendar():
    # 在下方写你的代码:获取2022年的HTML日期数据复制给data

    return render_template('review.html', data=data)


if __name__ == '__main__':
    app.run('127.0.0.1', 5001)
