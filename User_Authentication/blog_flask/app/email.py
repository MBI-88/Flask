# Packages
from threading import Thread
from flask import Flask, current_app, render_template
from flask_mail import Message
from . import mail

# Functions

def send_async_email(app:Flask,msg:str) -> None:
    with app.app_context():
        mail.send(msg)

def send_email(to:str,subject:str,template:str,**kwargs) -> Thread:
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' '+ subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr