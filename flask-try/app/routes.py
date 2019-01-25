from flask import render_template, flash, redirect, url_for
from app.form import loginform
from app import xyz
from app.post import post

@xyz.route('/')
@xyz.route('/index')
#route()是flask对象的一个方法
def index():
    user='Shadow'
    posts=post()
#    return "<h1>Hello, world!!!</h1>"
    return render_template('index.html',title='Home',user=user,posts=posts)

@xyz.route('/login', methods=['Get', 'Post'])
def login():
    form = loginform()
    if form.validate_on_submit():
        flash('login requested for {}'.format(form.username.date))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

@xyz.route('/no')
def no():
    return '234'

