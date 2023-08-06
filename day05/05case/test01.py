from flask import Flask, render_template

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/pig')
def index():
    return render_template('pig.html')


# 启动服务器程序
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001)
