# Script to make the Bluepint 

# Modules
from flask import Blueprint

# Main
main = Blueprint('main',__name__)

from . import views, errors