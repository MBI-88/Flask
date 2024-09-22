# API decorators
# Packages

from functools import wraps
from flask import g
from .errors import forbidden 

# Decorator

def permission_required(permission:int) -> object:
    def decorator(f:object) -> object:
        @wraps(f)
        def decorated_funcion(*args,**kwargs) -> object:
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args,**kwargs)
        return decorated_funcion
    return decorator