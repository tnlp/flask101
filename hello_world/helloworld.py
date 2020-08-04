from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/test')
def print():
    print(request.path)
    print(request.full_path)
    return request.args.__str__()

@app.route('/user/<int:id>')
def hello(id):
    return f'hello world!(id)'

@app.route('/register',methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'

@app.route('/get.html')
def get_html():
    # 使用render_template()方法重定向到templates文件夹下查找get.html文件
    return render_template('get.html')

@app.route('/post.html')
def post_html():
    return render_template('post.html')

@app.route('/deal_request', methods = ['GET', 'POST'])
def deal_request():
    if request.method == "GET":
        # get通过request.args.get("param_name","")形式获取参数值
        get_q = request.args.get("q","")
        return render_template("result.html", result=get_q)
    elif request.method == "POST":
        # post通过request.form["param_name"]形式获取参数值
        post_q = request.form["q"]
        return render_template("result.html", result=post_q)

if __name__=='__main__':
    app.run()