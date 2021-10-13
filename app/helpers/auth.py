from flask import abort

from app.models.user import User
from flask import flash


def assert_permit(session, permit_name):
    """Chequea que el usuario esté autenticado y autorizado."""
    if not authenticated(session):
        abort(401)

    if not session.get("user").has_permit(permit_name):
        abort(403)

def authenticated(session):
    """Devuelve el usuario guardado en la sesion."""
    return session.get("user")