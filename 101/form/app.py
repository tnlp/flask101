from forms import LoginForm
from flask import Flask,render_template
app=Flask(__name__)

app.secret_key='devops'
@app.route('/basic')
def basic():
    render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9990,debug=True)