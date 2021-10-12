from os import path, environ
from flask import Flask, render_template, g, Blueprint, session, redirect, url_for
from flask_session import Session
from config import config
from app import db
from app.resources import user, auth, palette, points
from app.helpers import handler
from app.helpers import auth as helper_auth
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )
    app.add_url_rule("/perfil", "auth_profile", auth.perfil)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new) 
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios", "user_modify", user.modify, methods=["PUT"])
    app.add_url_rule("/usuarios", "user_block", user.block, methods=["DELETE"])
    app.add_url_rule("/usuarios/alta", "user_unblock", user.unblock, methods=["PUT"])
    app.add_url_rule("/usuarios/rol", "user_assing_role", user.assign_role, methods=["POST"])
    app.add_url_rule("/usuarios/rol", "user_unassing_role", user.unassign_role, methods=["DELETE"])

    # Paleta de colores
    app.add_url_rule("/paleta_color", "paleta_index", palette.index)

    # Puntos de encuentro
    app.add_url_rule("/puntos_encuentro", "puntos_index", points.index)

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        if not helper_auth.authenticated(session):
            return redirect(url_for("auth_login"))

        return render_template("home.html", apartados=[
        {
            "nombre": "Paleta de colores",
            "url": url_for("paleta_index")
        },
        {
            "nombre": "Usuarios",
            "url": url_for("user_index")
        },
        {
            "nombre": "Perfil",
            "url": url_for("auth_profile")
        },
        {
            "nombre": "Puntos de encuentro",
            "url": url_for("puntos_index")
        },
        {
            "nombre": "Configuración",
            "url": ""
        }
    ])

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
