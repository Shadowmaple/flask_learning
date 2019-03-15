from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = 'Shadow <1142319190@qq.com>'
))
mail = Mail(app)


@app.route('/')
def index():
    msg = Message("Hello, world!",
            recipients=["654957943@qq.com"])
    msg.body = "email sender"
    mail.send(msg)
    return '<h3>Sended  email to U! ^^</h3>'

if __name__ == '__main__':
    app.run()

