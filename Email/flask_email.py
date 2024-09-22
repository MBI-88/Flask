# Script to develop flask emails

# Modules
from flask import Flask,session,redirect,url_for,render_template
from flask_mail import Mail, Message
import os
from formulary import User
from threading import Thread


# Functions
username = os.environ.setdefault('MAIL_USERNAME','')
password = os.environ.setdefault('MAIL_PASSWORD','')
adminEmail = os.environ.setdefault('FLASKY_ADMIN','admin@example.com')

print(username,' ',password,' ',adminEmail)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'M@ikel01*'
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
app.config['FLASKY_MAIL_SENDER'] = 'Flasky admin <flasky@example.com>'

mail = Mail(app)

def send_async_email(app:Flask,msg:Message) -> Mail:
    with app.app_context():
        mail.send(msg)


def send_mail(to:str, subject:str, template:str, **kwargs) -> Message:
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
                    sender = app.config['FLASKY_MAIL_SENDER'], recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thred = Thread(target = send_async_email, args = [app, msg]) # email asynchronous
    thred.start()
    #mail.send(msg)

@app.route('/', methods = ['GET','POST'])
def index() -> render_template:
     form = User()
     if (form.validate_on_submit()):
         session['name'] = form.name.data
         session['text'] = form.text.data
         if (app.config['FLASKY_ADMIN']):
             send_mail(app.config['FLASKY_ADMIN'], 'New User','mail/new_user',
                         user = {'name': session.get('name'),'text': session.get('text')})
             return redirect(url_for('success'))  
     return render_template('index.html',form = form, name = session.get('name'))

@app.route('/succes')
def success() -> render_template:
    return render_template('success.html')

# Main
if (__name__ == '__main__'):
    app.run(debug = True)

