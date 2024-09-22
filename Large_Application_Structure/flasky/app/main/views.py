# Script to make the blueprint'route

# Modules
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import MyForm
from .. import db
from ..models import User, Role

# Routes
@main.route('/', methods = ['GET','POST'])
def index() -> render_template:
    form = MyForm()
    user = ''
    role = ''
    if (form.validate_on_submit()):
        user = User.query.filter_by(username = form.name.data).first()
        if ( user is None):
            user = User(username = form.name.data)
            role = Role(name = form.role.data)
            db.session.add_all([user,role])
            session['known'] = False
            flash('Looks like you have changed your name!',category='message')

        else: session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        session['password'] = form.password.data
        form.password.data = ''
        session['role'] = form.role.data
        form.role.data = ''
        return redirect(url_for('.success'))
    
    return render_template('index.html',form = form, name = session.get('name'), 
                            current_time = datetime.utcnow())

@main.route('/success', methods = ['GET'])
def success() -> render_template:
    return render_template('success.html')
    
