# Script to handler erros

# Modules
from flask import render_template
from . import main

# Routes

@main.app_errorhandler(404)
def page_not_found(e:Exception) -> render_template:
    return render_template('404.hmtl'), 404

@main.app_errorhandler(500)
def internal_server_error(e:Exception) -> render_template:
    return render_template('500.html'), 500