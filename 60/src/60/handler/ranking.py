from flask import Blueprint, render_template, request, jsonify
from bson import ObjectId
from config import db

ranking = Blueprint('ranking', __name__)


# 显示排行榜
@ranking.route('/ranking', methods=['GET'])
def music_songs():
    # 在下方写你的代码：查询集合 ranking_type，获取'官方榜'文档
    pass
    # 获取官方榜下所有榜单

    # 获取第1个榜单文档

    # 获取第1个榜单下的歌曲，将其添加到列表中

    # 渲染返回 ranking.html 模板，通过模板变量 list、songs，传递所有榜单和首个榜单下的歌曲


# 获取榜单下的所有歌曲
@ranking.route('/music_list', methods=['GET'])
def get_music_list():
    # 获取榜单id
    rid = ObjectId(request.args.get('rid'))
    # 根据榜单id获取榜单文档
    ranking_info = db.ranking_list.find_one({'_id': rid})
    # 获取榜单下的歌曲id
    songs_id = ranking_info['songs_id']
    # 根据歌曲 id 获取歌曲，并添加到列表中
    ranking_songs = []
    for id in songs_id:
        song = db.songs.find_one({'_id': id})
        song['_id'] = str(song['_id'])
        ranking_songs.append(song)
    # 使用jsonify返回状态code为0，传递歌曲data
    return jsonify({'data': ranking_songs})
