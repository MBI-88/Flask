# Script to run app

# Modules
from flask import Flask,session,flash
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from webform import MyForm


# Functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'M1app'
Bootstrap(app)

@app.route('/',methods = ['GET','POST'])
def indexboostrap() -> render_template:
    old_name = session.get('name')
    form = MyForm()
    name = 'Stranger'
    if (form.validate_on_submit()):
        if (old_name is not None and old_name != form.name.data):
            flash('Looks like you have changed your name!',category='message')

        session['name'] = form.name.data
        session['password'] = form.password.data
        name = session.get('name')
        form.name.data = ''
        form.password.data = ''
        form.confirm.data = ''
    return render_template('indexbootstrap.html',name=name,form=form)



# Main
if (__name__ == "__main__"):
    app.run(debug=True)