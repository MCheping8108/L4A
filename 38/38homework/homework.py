from flask import Flask, render_template
import pymongo

# 连接数据库database38，向集合中插入文档数据
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['database38']
db.heros.delete_many({})
db.heros.insert_many(
    [
        {'name': '孙策', 'type': '战士', 'skill': '怒潮', 'partner': '哪吒、牛魔王'},
        {'name': '鲁班大师', 'type': '辅助', 'skill': '稷下科技', 'partner': '苏烈'},
        {'name': '李信', 'type': '战士', 'skill': '灰暗利刃', 'partner': '张飞、孙膑'},
        {'name': '张飞', 'type': '坦克', 'skill': '黑暗潜能', 'partner': '黄忠、后裔'},
        {'name': '杨玉环', 'type': '法师', 'skill': '惊鸿调', 'partner': '鲁班、程咬金'},
        {'name': '干将莫邪', 'type': '法师', 'skill': '比翼同心', 'partner': '钟无艳'},
        {'name': '司马懿', 'type': '刺客', 'skill': '静默之语', 'partner': '项羽、干将莫邪'},
        {'name': '花木兰', 'type': '战士', 'skill': '空烈斩', 'partner': '庄周、刘邦'},
        {'name': '妲己', 'type': '法师', 'skill': '失心', 'partner': '孙悟空、阿珂'},
        {'name': '大乔', 'type': '辅助', 'skill': '川流不息', 'partner': '狄仁杰、花木兰'}
    ]
)

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 查询所有
    data = list(db.heros.find({}))
    # 请在下方写你的代码:查询类型是辅助或者是战士的英雄文档

    return render_template('table.html', data=data)


app.run('127.0.0.1', 5000)
