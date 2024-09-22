#  Script to run app

# Modules
from flask import Flask,request,session,redirect,url_for,render_template,flash
from webform import MyForm


# Functions
app = Flask(__name__)
app.config['SECRET_KEY'] = 'M@ikel01*'

@app.route('/',methods = ['GET','POST'])
def index() -> render_template:
    form = MyForm()
    old_name = session.get('name')
    if ( request.method == 'POST' and form.validate_on_submit()):
        if (old_name is not None and old_name != form.name.data):
            flash('Looks like you have changed your nane!',category='message')
        session['name'] = form.name.data
        session['password'] = form.password.data
        session['confirm'] = form.confirm.data
        return redirect(url_for('success'))
    return render_template('index.html',form=form,name='')

@app.route('/success')
def success() -> render_template:
    return render_template('success.html',name=session.get('name'),password=session.get('password'))





# Main
if (__name__ == "__main__"):
    app.run(debug=True)
 
