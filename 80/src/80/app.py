from flask import Flask
from handler import user, shop
from datetime import timedelta
from data_init import data_import

app = Flask(__name__)

app.debug = True
app.send_file_max_age_default = timedelta(seconds=1)
app.config['SECRET_KEY'] = b'123456'

with app.app_context():
    data_import()

app.register_blueprint(user.user)
app.register_blueprint(shop.shop)

app.run('127.0.0.1', 8000)
