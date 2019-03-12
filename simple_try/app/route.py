from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, DataRequired
from flask_login import login_required, LoginManager, login_user, \
                    UserMixin, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'guess it'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'app.db')
#        'sqlite:///home/lawler/simple_try/app/a.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#是否追踪对象的修改并且发送信号

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

class RegistrationForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('Password')
    password1 = PasswordField('Repeat Password', 
            validators=[EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('login')

#需要'is_active'属性
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), index=True, unique=True)
    password = db.Column(db.String(12))

#用户加载函数(回调函数)记录用户登陆的数据，回调请求上下文来获取数据
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/index')
@app.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(2333)
        user = User(username=form.username.data, 
                password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.password is not form.password.data:
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or next_page is '/':
            return redirect(url_for('index'))
        return redirect(url_for(next_page))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()

