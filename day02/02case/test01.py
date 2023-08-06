from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/hello')
def hello():
    return render_template('test01.html')


# 打开调试模式
app.run(host='127.0.0.1', port=8001)
