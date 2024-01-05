from flask import abort, url_for


def assert_permit(session, permit_name):
    """Chequea que el usuario esté autenticado y autorizado."""
    if not authenticated(session):
        abort(401)

    if not has_permit(session, permit_name):
        abort(403)

def authenticated(session):
    """Devuelve el usuario guardado en la sesion."""
    return session.get("user")

def has_permit(session, permit_name):
    """Devuelve true si tiene el permiso enviado como parametro. De otra manera devolvera false."""
    permits = session.get("user_permits")
    if permits and permit_name in permits: 
        return True
    return False

def get_navigation_actions(session):
    if session.get("navigation_actions"):
        return session.get("navigation_actions")
    else:
        return generate_navigation_actions(session)

def generate_navigation_actions(session):
    actions = [
        {
            "nombre": "Configuración",
            "url": url_for("config_index"),
            "permit": "config_index"
        },
        {
            "nombre": "Puntos de encuentro",
            "url": url_for("points_index"),
            "permit": "points_index"
        },
        {
            "nombre": "Usuarios",
            "url": url_for("user_index"),
            "permit": "user_index"
        },
        {
            "nombre": "Zonas inundables",
            "url": url_for("fzone_index"),
            "permit": "fzone_index"
        },
        {
            "nombre": "Rutas de evacuación",
            "url": url_for("evroutes_index"),
            "permit": "evroutes_index"
        },
        {
            "nombre": "Denuncias",
            "url": url_for("complaint_index"),
            "permit": "complaint_index"
        }
    ]
    allowed_actions = []
    for action in actions:
        # allowed_actions.append(action)
        if has_permit(session, action["permit"]):
            allowed_actions.append(action)
            
    session["navigation_actions"] = allowed_actions
    return allowed_actions
