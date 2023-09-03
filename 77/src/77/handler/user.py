from flask import Blueprint, request, jsonify, session, redirect
from config import db

user = Blueprint('user', __name__)


# 实现注册功能
@user.route('/register', methods=['POST'])
def signup():
    # 在下方写你的代码:接收前端发送的用户名username以及密码 password
    pass
    # 如果用户名或者密码不存在，则返回响应，状态code为 1，提示信息data：参数错误
 
    # 查询该用户名文档，如果已经存在，则返回响应，状态code为 1，提示信息data：用户名已被注册

    # 以上情况均不存在，说明是合法的注册用户，在user集合中添加注册信息
    
    # 返回响应，状态code为 0，提示信息data：注册成功
   

# 实现登录功能
@user.route('/login', methods=['POST'])
def signin():
    # 在下方写你的代码：接收前端发送的用户名username以及密码 password
    pass
    # 根据用户名在user集合中查询用户信息
  
    # 如果不存在该用户信息，则返回响应，状态code为 1，提示信息data为：用户名不存在

    # 如果用户输入的密码和数据库中存储的密码不一致，则返回响应，状态code为 1，提示信息data为：密码不正确
 
    # 把用户文档user中的ObjectId对象转为字符串
    
    # 在session中保存用户信息user
   
    # 返回响应：状态code为 0 ，提示信息data为:登录成功
  













