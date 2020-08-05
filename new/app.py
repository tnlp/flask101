import os,sys
from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

WIN=sys.platform.startswith('win')

if WIN:
    prefix='sqlite:///'
else:
    prefix='sqlite:////'

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 主键 
    name = db.Column(db.String(20)) # 名字


class Movie(db.Model): # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True) # 主键 
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份

import click
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop')

def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database')

@app.cli.command()
def forge():
    db.create_all()
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("Done.")

@app.route('/')
def index():
    user=User.query.first()
    movies=Movie.query.all()
    return render_template('index.html', user=user, movies=movies)

@app.errorhandler(404)
def page_not_found(e):
    user=User.query.first()
    return render_template('404.html', user=user), 404 # 返回模 板和状态码
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000,debug=True)