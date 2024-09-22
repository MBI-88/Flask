# Example 2-1.hello.py Acomplete Flask application

# Modules
from flask import Flask

# Funcions
app = Flask(__name__)

@app.route('/')
def index() -> str:
    return '<h1>Hello World!</h1>'

# New function (Example 2-2.hello.py Flask application with a dynamic route)
@app.route('/user/<name>')
def user(name) -> str:
    return '<h1>Hello, %s!</h1>' % name



# Maiin
if __name__=='__main__':
    app.run(debug=True)
  