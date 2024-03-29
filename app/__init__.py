from os import path, environ, urandom
from json import dumps as json_dumps

from flask import Flask, render_template, g, Blueprint, session, redirect, url_for, make_response, send_from_directory
from flask_session import Session
from flask_cors import CORS

from config import config
from app import db
from app.resources import user, auth, points, flood_zone, complaint, evacuation_routes, config as configObject
from app.resources import follow_up, palettes
from app.resources.config import Config
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.resources.api.flood_zone import flood_zone_api
from app.resources.api.complaint import complaint_api
from app.resources.api.evacuation_routes import evacuation_routes_api
from app.resources.api.meeting_points import meeting_points_api
from app.resources.api.statistics import statistics_api


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Configuracion de CORS (Cross Origin Resource Sharing)
    CORS(app)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Configuracion de OAuth
    app.secret_key = environ.get("SECRET_KEY") or urandom(24)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(get_navigation_actions=helper_auth.get_navigation_actions)
    # app.jinja_env.globals.update(private_theme=configObject.get_private_palette)
    app.jinja_env.globals.update(private_theme=Config.get_private_palette)
    app.jinja_env.globals.update(parsed_coordinates=evacuation_routes.parse_coordinates)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )
    app.add_url_rule(
        "/autenticacion/social", "auth_authenticate_social", auth.google_login
    )
    app.add_url_rule(
        "/login/callback", "auth_callback", auth.callback, methods=["GET"]
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
    app.add_url_rule("/usuarios/approve/<int:user_id>", "user_approve", user.approve, methods=["GET", "POST"])

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

    # Rutas de denuncias
    app.add_url_rule("/denuncias", "complaint_index", complaint.index)
    app.add_url_rule("/denuncias/show/<int:complaint_id>", "complaint_show", complaint.show, methods=["GET"])
    app.add_url_rule("/denuncias/modify/<int:complaint_id>", "complaint_modify", complaint.modify, methods=["GET", "POST"])
    app.add_url_rule("/denuncias/nuevo", "complaint_new", complaint.new, methods=["GET", "POST"])
    app.add_url_rule("/denuncias", "complaint_create", complaint.create, methods=["GET", "POST"])
    app.add_url_rule("/denuncias/delete/<int:complaint_id>", "complaint_delete", complaint.delete, methods=["GET", "POST"])
    app.add_url_rule("/denuncias/close/<int:complaint_id>", "complaint_close", complaint.close_complaint, methods=["GET", "POST"])

    # Rutas de seguimientos
    app.add_url_rule("/seguimientos/<int:complaint_id>", "follow_up_index", follow_up.index)
    app.add_url_rule("/seguimientos/modify/<int:follow_up_id>", "follow_up_modify", follow_up.modify, methods=["GET", "POST"])
    app.add_url_rule("/seguimientos/nuevo/<int:complaint_id>", "follow_up_new", follow_up.new, methods=["GET", "POST"])
    app.add_url_rule("/seguimientos/", "follow_up_create", follow_up.create, methods=["GET", "POST"])
    app.add_url_rule("/seguimientos/delete/<int:follow_up_id>", "follow_up_delete", follow_up.delete, methods=["GET", "POST"])

    # Rutas de rutas de evacuacion
    app.add_url_rule("/rutas_evacuacion", "evroutes_index", evacuation_routes.index)
    app.add_url_rule("/rutas_evacuacion/show/<int:evroute_id>", "evroutes_show", evacuation_routes.show, methods=["GET"])
    app.add_url_rule("/rutas_evacuacion/nuevo", "evroutes_new", evacuation_routes.new, methods=["GET", "POST"])
    app.add_url_rule("/rutas_evacuacion", "evroutes_create", evacuation_routes.create, methods=["GET", "POST"])
    app.add_url_rule("/rutas_evacuacion/modify/<int:evroute_id>", "evroutes_modify", evacuation_routes.modify, methods=["GET", "POST"])
    app.add_url_rule("/rutas_evacuacion/delete/<int:evroute_id>", "evroutes_delete", evacuation_routes.delete, methods=["GET", "POST"])

    # Rutas de Config
    app.add_url_rule("/config", "config_index", configObject.index)
    app.add_url_rule("/config/modify", "config_modify", configObject.modify, methods=["GET", "POST"])

    # Rutas de Puntos de encuentro
    app.add_url_rule("/paletas", "palettes_index", palettes.index)
    app.add_url_rule("/paletas/show/<int:palette_id>", "palettes_show", palettes.show, methods=["GET"])
    app.add_url_rule("/paletas/modify/<int:palette_id>", "palettes_modify", palettes.modify, methods=["GET", "POST"])
    app.add_url_rule("/paletas/nuevo", "palettes_new", palettes.new, methods=["GET", "POST"])
    app.add_url_rule("/paletas", "palettes_create", palettes.create, methods=["GET", "POST"])
    app.add_url_rule("/paletas/delete/<int:palette_id>", "palettes_delete", palettes.delete, methods=["GET", "POST"])


    # Ruta para el Home (usando decorador)
    @app.route("/")
    def home():
        if not helper_auth.authenticated(session):
            return redirect(url_for("auth_login"))

        return render_template("generic/pages/home.html")


    @app.route("/sw.js", methods=["GET"])
    def sw():
        return app.send_static_file("sw.js")


    @app.route("/manifest.webmanifest", methods=["GET"])
    def manifest():
        return app.send_static_file("manifest.webmanifest")


    @app.route("/_allowed_pages", methods=["GET"])
    def allowed_pages():
        nav_actions = helper_auth.get_navigation_actions(session)
        actions_url = [x["url"] for x in nav_actions] if nav_actions else nav_actions
        response = make_response(json_dumps(actions_url, indent=4, ensure_ascii=False))
        response.headers['Content-Type'] = 'application/json'
        return response


    @app.route("/offline", methods=["GET"])
    def offline():
        return render_template("generic/pages/offline.html")


    # Rutas de la API
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(flood_zone_api)
    api.register_blueprint(complaint_api)
    api.register_blueprint(evacuation_routes_api)
    api.register_blueprint(meeting_points_api)
    api.register_blueprint(statistics_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(400, handler.bad_request_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.forbidden_error)
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(500, handler.internal_server_error)

    # Retornar la instancia de app configurada
    return app
