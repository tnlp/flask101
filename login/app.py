from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/signin',methods=['GET'])
def signin():
    return render_template('form.html')

# 登录表单
@app.route('/signin',methods=['POST'])
def signin_from():
    # 获取表单的数据，判断逻辑
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return render_template('sign-ok.html',username = username);
    return render_template('from.html',message = '用户名或密码错误',username = username)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000,debug=True)