from config import db

if __name__ == '__main__':
    # 在下方写你的代码：删除xiaoming用户
    db.user.delete_one({'username': 'xiaoming'})

    users = db.user.find()
    for user in users:
        print(user)
