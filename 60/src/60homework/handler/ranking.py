from flask import Blueprint, render_template, request, jsonify
from bson import ObjectId
from config import db

ranking = Blueprint('ranking', __name__)


# 显示排行榜
@ranking.route('/ranking', methods=['GET'])
def music_songs():
    # 查询集合 ranking_type，获取'官方榜'文档
    ranking_type = db.ranking_type.find_one({'name': '官方榜'})
    # 获取官方榜下所有榜单
    ranking_list = ranking_type['ranking_list']

    # 获取第1个榜单文档
    name = ranking_list[0]['name']
    ranking = db.ranking_list.find_one({'name': name})
    # 获取第1个榜单下的歌曲，将其添加到列表中
    songs_id = ranking['songs_id']
    ranking_songs = []
    for id in songs_id:
        ranking_songs.append(db.songs.find_one({'_id': id}))
    # 渲染返回 ranking.html 模板，通过模板变量 list、songs，传递所有榜单和首个榜单下的歌曲
    return render_template('ranking.html', list=ranking_list, songs=ranking_songs)


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


# 获取榜单类别下的榜单
@ranking.route('/getRanking', methods=['GET'])
def get_ranking():
    # 在下方写你的代码：通过 'key' 获取前端传递的榜单类别名称
    pass
    # 根据榜单类别名称，查询集合 ranking_type 获取榜单类别文档

    # 通过 'ranking_list' 获取榜单类别文档中的所有榜单

    # 遍历榜单，将 ObjectId 对象通过 str() 转场字符串

    # 调用 jsonify() 返回数据 {'data':榜单列表}








