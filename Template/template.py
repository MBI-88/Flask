# Example 3-3.hello.py Rendering a tample

# Modules
import re
from flask import Flask,render_template,url_for,redirect,request
from flask.wrappers import Request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

# Functions
app = Flask(__name__)
Bootstrap(app)
Moment(app)

@app.route('/')
def index() -> render_template:
    return render_template('index.html')

@app.route('/user/<name>')
def user(name) -> render_template:
    return render_template('user.html',name=name)

@app.route('/bootstrap/<name>')
def userbootstrap(name,current_time=None) -> render_template:
    return render_template('bootstrap.html',name=name,current_time=datetime.utcnow())

@app.route('/bootstrapnav/')
def bootsNav() -> render_template:
    return render_template('bootstrapnav.html')

@app.errorhandler(404)
def page_not_found(e) -> render_template:
    return render_template('Error404.html'),404

@app.errorhandler(500)
def internal_server_error(e) -> render_template:
    return render_template('InternalServerError.html'),500

@app.route('/visitaForm/',methods=['GET','POST'])
def visitaUrl() -> render_template:
    if (request.method == 'POST'):
        return redirect(url_for('index'))
    
    return render_template('visitaForm.html')
    




# Main
if (__name__ == '__main__'):
    app.run(debug=True)