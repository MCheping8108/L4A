from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('test01.html')


if __name__ == '__main__':
    app.run(port=8001)
