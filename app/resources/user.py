from flask import redirect, render_template, request, url_for, session, abort
from app.models.user import User
from app.helpers.auth import authenticated
import app.db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.all()
    
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    User.create(**request.form)

    return redirect(url_for("user_index"))