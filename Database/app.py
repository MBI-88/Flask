from flask_migrate import Migrate
from flask_database import app, db

# It recomended using this file for the connection each other script

migrate = Migrate()

def create_app():
    db.init_app(app)
    migrate.init_app(app, db)
    return app