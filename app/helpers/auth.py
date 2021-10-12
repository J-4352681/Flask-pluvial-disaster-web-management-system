from sqlalchemy.sql.expression import false, true


def authenticated(session):
    return session.get("user")

def authorized(session, permit_name):
    """Devuelve true si el usuario enviado como parametro tiene el permiso envido como parametro. De otra manera devolvera false."""
    actual_user = session.get("user")
    for rol in actual_user.roles:
        for permiso in rol.permits:
            if( permit_name == permiso.name):
                return true

    return false