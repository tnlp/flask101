from flask import Flask,request,redirect,url_for,abort,make_response,json,render_template
from flask import jsonify,session
import os
app=Flask(__name__)

@app.route('/hello')

def hello():
    name=request.args.get('name','flask')
    return '<h1>hello,%s</h1>' % name
@app.route('/hellos',methods=['GET','POST'])
def hellos():
    #return 'hello world',201 
    name=request.args.get('name')
    if name is None:
        name=request.cookies.get('name','Human')
    return '<h1>hello, %s</h1>' % name
@app.route('/redirects')
def redirects():
    return redirect('https://www.baidu.com/')


@app.route('/test')
def test():
    return redirect(url_for('hello'))


@app.route('/goback/<int:year>')
def go_bback(year):
    return '<p> Welcome to %d </p>' %(2018-year)
@app.route('/foo')

def foo():
    response=make_response('hello,word')
    response.mimetype='test/plain'
    return response

@app.route('/foo1')
def foo1():
    data={
        'name':'Grey Li',
        'gender':'male'
    }
    response=make_response(json.dumps(data))
    response.mimetype='application/json'
    return response
@app.route('/foo2')
def foo2():
    return jsonify({'name':'Eric Zhou','age':22,'gender':'male'})

@app.route('/set/<name>')
def set_cookie(name):
    response=make_response(redirect(url_for('hellos')))
    response.set_cookie('name',name)
    return response

@app.route('/404')
def not_found():
    abort(404)

app.secret_key='devops@2020'

@app.route('/login')
def login():
    session['logged_in']=True
    return redirect(url_for('demo'))
@app.route('/demo')
def demo():
    name=request.args.get('name')
    if name is None:
        name=request.cookies.get('name','test')
        response='hello ,%s' % name
        if 'logged_in' in session:
            response+='[Authenticated]'
        else:
            response+='[Not Authenticated]'
        return response
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'welcome to admin page'

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('demo'))  

user={
    'username':'Grey Li',
    'bio': 'A boy loves movies and music.'
}

movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'}, {'title': 'King of Comedy', 'year': '1999'}, {'title': 'Devils on the Doorstep', 'year': '1999'}, {'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies=movies)
@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=7000,debug=True)