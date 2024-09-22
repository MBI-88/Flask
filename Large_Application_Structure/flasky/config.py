# Script to configure the Flask'app

# Modules
import os

# Classes
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '1024'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','')

    @staticmethod
    def init_app(app) -> None:
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_USE_TLS = False # recomended True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')  or 'sqlite:///' + os.path.join(basedir,'devdb.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')  or 'sqlite:///' + os.path.join(basedir,'testdb.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  or 'sqlite:///' + os.path.join(basedir,'prodb.sqlite')



config:dict[str,object] = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
