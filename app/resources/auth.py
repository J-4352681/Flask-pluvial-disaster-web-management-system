from flask import redirect, render_template, request, url_for, abort, session, flash
from app.models.user import User


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form

    user = User.find_by_email_and_password(params["email"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    session["user"] = user
    session["user_permits"] = set([permit.name for permits in map(lambda rol: rol.permits, user.roles) for permit in permits])
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))

def perfil():
    return render_template("user/perfil.html")
