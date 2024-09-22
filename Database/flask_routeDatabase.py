# Script to access database

# Modules
from webform import MyForm
from flask import session,redirect,render_template,url_for
from flask_database import User,db,app

# Functions
app.config['SECRET_KEY'] = 'In1cioD@tab@se'

@app.route('/',methods = ['GET','POST'])
def index() -> render_template:
    form = MyForm()
    if (form.validate_on_submit()):
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(usernames = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('completed'))
    return render_template('indexFormDatabase.html',form = form, name = session.get('name'),known = session.get('known', False)) 

@app.route('/completed')
def completed() -> render_template:
    return render_template('completed.html')

# Main 
if (__name__ == "__main__"):
    app.run(debug = True)