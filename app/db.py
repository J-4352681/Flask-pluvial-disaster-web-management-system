from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


def init_app(app):
    db.init_app(app)
    config_db(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()
    
    @app.teardown_request
    def close_session(exception=None):
        db.session.remove() 
