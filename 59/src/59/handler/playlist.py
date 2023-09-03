from flask import Blueprint, render_template, request, jsonify
from config import db, get_music_url
from bson import ObjectId

playlist = Blueprint('playlist', __name__)


# 获取歌曲播放链接
@playlist.route('/getUrl', methods=['POST'])
def ger_url():
    url = request.form.get('url')
    return jsonify(get_music_url(url))


# 显示首页，默认显示‘推荐’
@playlist.route('/index', methods=['GET'])
def music_index():
    # 在下方写你的代码：查询集合 play_list，按播放量 listencnt 降序排列，取前5条文档
    pass
    # 渲染返回index.html页面，通过模板变量 plist 将上一步获得的数据传递给模板文件


# 显示歌单详情，及歌单中的歌曲
@playlist.route('/plist', methods=['GET'])
def play_list():
    # 在下方写你的代码：获取请求参数歌单id
    pass
    # 根据 id 从集合 play_list 中查询歌单文档

    # 遍历歌单文档中 songs_id 字段的列表

        # 根据歌曲id 从集合 songs 中查询歌曲文档，保存在列表中

    # 渲染返回 playlist.html 页面，通过模板变量 play_list 将上一步获得的数据传递给模板文件











