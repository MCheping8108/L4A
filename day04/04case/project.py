from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/<name>')
def student(name):
    return render_template(name + '.html')


app.run(host='127.0.0.1', port=8000)
