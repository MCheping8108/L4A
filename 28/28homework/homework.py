from flask import Flask
from handler import pixar_study, pixar_stories

web = Flask(__name__)

# 请在下方写你的代码:注册 pixar_study 和 pixar_stories 蓝图
web.register_blueprint(pixar_study.bp)
web.register_blueprint(pixar_stories.bp)



web.run(host='127.0.0.1', port=5007)
