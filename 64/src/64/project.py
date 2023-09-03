import calendar
from flask import Flask, request, render_template

app = Flask(__name__)
# 注册蓝图
app.debug = True


@app.route('/calendar')
def get_calendar():
    # 在下方写你的代码：获取请求参数年份，转为整数类型
    pass
    # 实例化 HTML 日历类

    # 获取指定年份的 HTML 日历

    # 渲染 calendar.html，返回模板变量data


if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
