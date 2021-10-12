from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from app.models.user import User
from app.helpers.auth import authenticated, authorized
import app.db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.all()
    
    return render_template("user/index.html", users=users)