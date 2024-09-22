# Modules
from flask import Blueprint

# Main
main = Blueprint('main',__name__)

from . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions() -> dict:
    return dict(Permission = Permission)