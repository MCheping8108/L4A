# 请在下方写你的代码
from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route('/hello')

def hello():
    return "你好，同志"
app.run(host='localhost', port=8001)