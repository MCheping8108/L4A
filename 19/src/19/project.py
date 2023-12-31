from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
    {'username': 'xiaoshan', 'password': '123456'},
    {'username': 'xiaojing', 'password': '000000'},
    {'username': 'xiaoqi', 'password': '888888'}
]


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


photos = [
    {'title': '海浪', 'cover': 'item-19.jpg', 'content': '海就是海,有着跳动不息的脉搏,有一腔奔腾不息的热血'},
    {'title': '向日葵', 'cover': 'item-18.jpg', 'content': '哪怕太阳只停留一秒钟,向日葵也会微笑的绽放'},
    {'title': '椰子树', 'cover': 'item-17.jpg', 'content': '春雨蒙蒙，椰子树吮吸着这甘露似的雨水，舒展起绿莹莹的长叶子，好像一位荷枪待征抄的士兵'},
    {'title': '海滩', 'cover': 'item-16.jpg', 'content': '海边溅起了的洁白晶莹的水花，轻轻地抚摩着细软的沙滩，又恋恋不舍地退回'},
    {'title': '玫瑰', 'cover': 'item-15.jpg', 'content': '远远看上去,一株株玫瑰花显现出一片红色,红似火,艳如霞,美丽极了'},
    {'title': '金沙', 'cover': 'item-14.jpg', 'content': '远看它像金色的沙滩泛海水的光亮，走近看它像金黄色的小嗽叭'},
    {'title': '水母', 'cover': 'item-13.jpg', 'content': '在左海的海底世界，我看见了一把把游动的小伞——水母'},
    {'title': '火焰', 'cover': 'item-12.jpg', 'content': '火就是希望，人类有了火，便拥有了生存与发展的基本力量'},
    {'title': '黄昏', 'cover': 'item-11.jpg', 'content': '我滑下你的暮色如同厌倦滑落度下一道斜坡的虔诚，年轻的夜晚像你屋顶平台上的一片翅膀'},
    {'title': '候鸟', 'cover': 'item-10.jpg', 'content': '候鸟失逢应垂泪，来年长白夏谷堆'},
    {'title': '月亮', 'cover': 'item-9.jpg', 'content': '夜晚，满月升起来了，一片宁静随着银雾般的月光洒在大地上'},
    {'title': '向往', 'cover': 'item-8.jpg', 'content': '你最向往的日子是什么样子的，你做到了么，会有那一天么'}
]

# 在下方写你的代码：设置路由，返回首页

@app.route('/')
def home():
    # 在下方写你的代码：传递模板变量给前端模板文件
    return render_template('index.html', photos=photos)
    # return render_template('index.html')


# 在下方写你的代码：设置路由，返回登录页面

@app.route('/login')
def login():
    # 在下方写你的代码：传递模板变量给前端模板文件
    return render_template('login.html')



app.run(host='127.0.0.1', port=8000)
