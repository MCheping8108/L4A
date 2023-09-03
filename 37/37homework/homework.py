from flask import Flask, render_template
import pymongo

# 连接数据库database37，向集合products插入文档数据
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['database37']
db.products.delete_many({})
db.products.insert_many(
    [
        {"product": "MacBookAir", "type": "电脑", "price": 6999, "company": "苹果"},
        {"product": "MacBookPro低配版", "type": "电脑", "price": 14299, "company": "苹果"},
        {"product": "MacBookPro高配版", "type": "电脑", "price": 22850, "company": "苹果"},
        {"product": "IPhone XS Max", "type": "手机", "price": 9199, "company": "苹果"},
        {"product": "Galaxy S10", "type": "手机", "price": 5999, "company": "三星"},
        {"product": "荣耀MagicBook", "type": "电脑", "price": 3999, "company": "华为"},
        {"product": "P30 pro", "type": "手机", "price": 5999, "company": "华为"},
    ]
)

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/data', methods=['GET'])
def show_data():
    # 查询所有
    data = list(db.products.find({}))
    # 下方写你的代码:查询苹果公司出品的电脑都有哪些
    

    return render_template('table.html', data=data)


app.run('127.0.0.1', 5000)
