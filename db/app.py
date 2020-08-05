from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

"""
flask shell
from app import db
db.create_all()
from app import User
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
"""
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
"""
# 创建 User 对象
class Users(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    def __repr__(self):
        return '<User %r>' % self.username
# 创建表
db.create_all()

us1=Users(username='wang',email='wang@qq.com',password='123456')
db.session.add(us1)
us2=Users(username='zhou',email='zhou@qq.com',password='123456')
db.session.add(us2)
us3=Users(username='he',email='he@qq.com',password='123456')
db.session.add(us3)
# 查询数据
user = Users.query.filter(Users.username == 'wang').first()
print(user)

# 修改
wang = Users.query.filter(Users.username == 'wang').first()
wang.email = "email@qq.com"
db.session.commit()
wang = Users.query.filter(Users.username == 'wang').first()
print(wang,wang.email,wang.password,wang.register_time)

# 删除
# result = Users.query.filter(Users.username == 'wang').first()
# db.session.delete(result)

# 查询10条记录
#users = Users.query.limit(10).all()
users=Users.query.all()
print(users)
# 查询所以数据
result = Users.query.all()
print(user)

#http://www.pythondoc.com/flask-sqlalchemy/queries.html