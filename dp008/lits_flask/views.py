from flask import flash, render_template, redirect

from app import app
from forms import LoginForm
from models import User


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(login_form.password.data):
            return redirect('/')
        else:
            flash('Username or password are not valid')
    return render_template('login.html', form=login_form)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/ajax")
def ajax():
    return {'result': 'OK'}


@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route("/<name>")
def hello_name(name):
    # get 10 records from DB
    users = ['user1', 'user2', 'user3', 'user4']
    return render_template('index.html', username=name,
                           users=users)
