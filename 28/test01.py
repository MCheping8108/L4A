from flask import Flask

from handler import wm_game, wm_store

web = Flask(__name__)
web.debug = True

# 请在下方写你的代码：注册wm_game和wm_store模块中蓝图
web.register_blueprint(wm_game.bp)
web.register_blueprint(wm_store.bp)

web.run(host='127.0.0.1', port=8001)
