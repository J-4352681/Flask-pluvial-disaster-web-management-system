from flask import abort
from sqlalchemy.sql.expression import false, true


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
    user = session.get("user")
    for rol in user.roles:
        if (permit_name in map(lambda x: x.name, rol.permits)):
            return true

    return false