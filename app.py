"""Blogly application."""

from flask import Flask, render_template, session, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cows'
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
# db.create_all()

@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def users():
    total = []
    currentusers = User.query.all()
    for user in currentusers:
        u = []
        u.append(user.first_name)
        u.append(user.last_name)
        u.append(user.image_url)
        u.append(user.id)
        total.append(u)
        print(total)
    return render_template('user.html', total=total)
# , total=total

@app.route('/users/<userid>')
def userId(userid):
    top = []
    id=int(userid)
    userpage = User.query.get(id)
    # print(userpage[0])
    # for user in userpage:
    #     top.append(user[0])
    #     top.append(user[1])
    #     top.append(user[2])
    #     print(top)
    return render_template('user_page.html', userpage=userpage)


@app.route('/users/new', methods=['POST', 'GET'])
def newUser():
    if request.method == 'POST':
        print('this was a post request')
        firname = request.form['f_name']
        print(firname)
        lasname = request.form['l_name']
        print(lasname)
        imgurl = request.form['img_url']
        
        newUser = User(first_name=firname, last_name=lasname, image_url=imgurl)
        db.session.add(newUser)
        db.session.commit()
        
        return redirect('/users')

    else:
        return render_template('new-user-form.html')


@app.route('/users/<userid>/edit', methods=['POST', 'GET'])
def user_id_edit(userid):
    if request.method == 'POST':
        return 'Your info has been changed!'
    else:
        top = []
        id=int(userid)
        userpage = User.query.get(id)
        top.append(userpage.first_name)
        top.append(userpage.last_name)
        top.append(userpage.image_url)
        # top.append(userpage.id)
        print (top)
        return render_template('user_edit.html', top=top) 