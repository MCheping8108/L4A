import pymongo


def create_market():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['database36']
    b = list(db.cart.find())
    if len(b) <= 0:
        db.cart.insert_many(
            [
                {'name': '可乐', 'number': 2, 'cost': 10},
                {'name': '薯条', 'number': 5, 'cost': 50},
                {'name': '牛奶', 'number': 10, 'cost': 30},
                {'name': '饼干', 'number': 1, 'cost': 15}
            ]
        )
    return db


db = create_market()

if __name__ == '__main__':
    # 在下方写你的代码： 更新可乐的数量和金额，数量number加1，金额cost加5
   
    for cart in db.cart.find():
        print(cart)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
