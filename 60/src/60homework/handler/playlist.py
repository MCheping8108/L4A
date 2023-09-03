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
    # 查询集合 play_list，按播放量 listencnt 降序排列，取前5条文档
    plist = list(db.play_list.find().sort('listencnt', -1).limit(5))
    # 渲染返回index.html页面，通过模板变量 plist 将上一步获得的数据传递给模板文件
    return render_template('index.html', plist=plist)


# 显示歌单详情，及歌单中的歌曲
@playlist.route('/plist', methods=['GET'])
def play_list():
    # 获取请求参数歌单id
    id = ObjectId(request.args.get('id'))
    # 根据 id 从集合 play_list 中查询歌单文档
    play_list = db.play_list.find_one({'_id': id})

    # 遍历歌单文档中 songs_id 字段的列表
    play_list['songs'] = []
    for id in play_list['songs_id']:
        # 根据歌曲id 从集合 songs 中查询歌曲文档，保存在列表中
        song = db.songs.find_one({'_id': id})
        play_list['songs'].append(song)
    # 渲染返回 playlist.html 页面，通过模板变量 play_list 将上一步获得的数据传递给模板文件
    return render_template('playlist.html', play_list=play_list)


# 显示歌单
@playlist.route('/list', methods=['GET'])
def music_list():
    # 查询 play_list 集合获取所有歌单，并调用 list 函数将查询结果转成列表。
    plist = list(db.play_list.find())
    # 渲染返回模板文件 list.html，并通过模板变量 plist 传递歌单列表给模板文件。
    return render_template('list.html', plist=plist)

















