from os import path, environ
import logging

from flask import Flask, render_template, g, Blueprint, session, redirect, url_for
from flask_session import Session

from config import config
from app import db
from app.resources import user, auth, points, flood_zone, config as configObject
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.resources.api.flood_zone import flood_zone_api
from app.resources.api.complaint import complaint_api

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
    app.jinja_env.globals.update(get_navigation_actions=helper_auth.get_navigation_actions)
    app.jinja_env.globals.update(private_theme=configObject.getPrivatePalette)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new, methods=["GET", "POST"]) 
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/modify/<int:user_id>", "user_modify", user.modify, methods=["GET", "POST"])
    app.add_url_rule("/usuarios/borrar/<int:user_id>", "user_delete", user.delete, methods=["GET", "POST"])
    app.add_url_rule("/usuarios/baja/<int:user_id>", "user_block", user.block, methods=["GET", "POST"])
    app.add_url_rule("/usuarios/alta/<int:user_id>", "user_unblock", user.unblock, methods=["GET", "POST"])
    app.add_url_rule("/usuarios/rol", "user_assing_role", user.assign_role, methods=["POST"])
    app.add_url_rule("/usuarios/rol", "user_unassing_role", user.unassign_role, methods=["DELETE"])
    app.add_url_rule("/perfil", "profile_index", user.profile)
    app.add_url_rule("/perfil/edit", "profile_modify", user.profile_modify, methods=["GET", "POST"])

    
    # Rutas de Puntos de encuentro
    app.add_url_rule("/puntos_encuentro", "points_index", points.index)
    app.add_url_rule("/puntos_encuentro/show/<int:point_id>", "points_show", points.show, methods=["GET"])
    app.add_url_rule("/puntos_encuentro/modify/<int:point_id>", "points_modify", points.modify, methods=["GET", "POST"])
    app.add_url_rule("/puntos_encuentro/nuevo", "points_new", points.new, methods=["GET", "POST"]) 
    app.add_url_rule("/puntos_encuentro", "points_create", points.create, methods=["GET", "POST"])
    app.add_url_rule("/puntos_encuentro/delete/<int:point_id>", "points_delete", points.delete, methods=["GET", "POST"])

    # Rutas de zonas inundables
    app.add_url_rule("/zonas_inundables", "fzone_index", flood_zone.index)
    app.add_url_rule("/zonas_inundables/show/<int:fzone_id>", "fzone_show", flood_zone.show, methods=["GET"])
    app.add_url_rule("/zonas_inundables/modify/<int:fzone_id>", "fzone_modify", flood_zone.modify, methods=["GET", "POST"])
    app.add_url_rule("/zonas_inundables/nuevo", "fzone_new", flood_zone.new, methods=["GET", "POST"])
    app.add_url_rule("/zonas_inundables/", "fzone_create", flood_zone.create, methods=["GET", "POST"])
    app.add_url_rule("/zonas_inundables/delete/<int:fzone_id>", "fzone_delete", flood_zone.delete, methods=["GET", "POST"])
    app.add_url_rule("/zonas_inundables/csvimport", "fzone_csvimport", flood_zone.csv_import, methods=["GET", "POST"])

    # Rutas de Config
    app.add_url_rule("/config", "config_index", configObject.index)
    app.add_url_rule("/config/modify", "config_modify", configObject.modify, methods=["GET", "POST"])

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        if not helper_auth.authenticated(session):
            return redirect(url_for("auth_login"))

        return render_template("home.html")

    # Rutas de la API
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(flood_zone_api)
    api.register_blueprint(complaint_api)
    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(400, handler.bad_request_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.forbidden_error)
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(500, handler.internal_server_error)

    # Retornar la instancia de app configurada
    return app
