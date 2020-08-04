from flask import Flask
import pymysql
app=Flask(__name__)
db = pymysql.connect("localhost", "root", "", "demo")
# 新建游标
cursor = db.cursor()
# 执行sql语句
cursor.execute("select * from person")
data = cursor.fetchone()
print(data)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)