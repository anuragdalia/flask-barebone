from functools import wraps

from flask_login import current_user

from main import lm
from database.models import Roles


def login_required(role=Roles.BOTOWNER):
    def decorator(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return lm.unauthorized()
            if role == Roles.ALL:
                return fn(*args, **kwargs)
            elif role == Roles.BOTOWNER and current_user.get_urole() not in [Roles.BOTOWNER, Roles.ALL]:
                return "You should be atleast a {}".format(role)
            elif role == Roles.SUPERVISOR and current_user.get_urole() not in [Roles.SUPERVISOR, Roles.BOTOWNER, Roles.ALL]:
                return "You should be atleast a {}".format(role)
            else:
                return fn(*args, **kwargs)
            # add more elifs when you add more user roles

        return decorated_view

    return decorator
