from flask import Flask, render_template, jsonify, request
from player_init import db

app = Flask(__name__)
app.debug = True


@app.route('/player', methods=['GET'])
def player_ability():
    return render_template('project.html')


@app.route('/info', methods=['GET'])
def player_info():
    # 获取选择的球员
    player = request.args.get('player')
    # 统计职业生涯的场均得分总和
    player_info = list(db.players.find({'player': player}))
    total_score = sum([r['score'] for r in player_info])
    total_rebound = sum([r['rebound'] for r in player_info])
    total_assists = sum([r['assists'] for r in player_info])
    total_steals = sum([r['steals'] for r in player_info])
    total_blocking = sum([r['blocking'] for r in player_info])
    # 在下方写你的代码：获取球员赛季数，赋值给count变量


    # 求平均分
    data = {
        'score': total_score / count,
        'rebound': total_rebound / count,
        'assists': total_assists / count,
        'steals': total_steals / count,
        'blocking': total_blocking / count
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
