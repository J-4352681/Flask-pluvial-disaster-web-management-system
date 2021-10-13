from flask import abort

from app.models.user import User
from flask import flash


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
    """Devuelve true si el usuario enviado como parametro tiene el permiso envido como parametro. De otra manera devolvera false."""
    user = User.find_by_username(session.get("user").username)
    for rol in user.roles:
        if permit_name in map(lambda x: x.name, rol.permits):
            return True

    return False