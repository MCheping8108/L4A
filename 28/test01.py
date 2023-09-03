from flask import Flask

web = Flask(__name__)
web.debug = True

# 请在下方写你的代码：注册wm_game和wm_store模块中蓝图


web.run(host='127.0.0.1', port=8001)
