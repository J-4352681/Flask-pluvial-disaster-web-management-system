from flask import redirect, render_template, request, url_for, abort, session, message_flashed, flash
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
    session["user_permits"] = user.get_permits()
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    del session["user"]
    del session["user_permits"]
    del session["navigation_actions"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))

def perfil():
    return render_template("user/perfil.html")
