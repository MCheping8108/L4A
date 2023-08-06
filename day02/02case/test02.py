# 从flask模块中导入render_template函数
from flask import Flask, render_template

app = Flask(__name__)

app.debug = True


@app.route('/test02')
def test02():
    return render_template('test02.html')


app.run(host='127.0.0.1', port=8001)
