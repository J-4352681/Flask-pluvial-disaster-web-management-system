from os import environ

from sqlalchemy.sql.expression import false


class Config(object):
    """Base configuration."""

    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class ProductionConfig(Config):
    """Production configuration."""

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "grupo38")
    DB_PASS = environ.get("DB_PASS", "NjIxMzkyZjYwYTM4")
    DB_NAME = environ.get("DB_NAME", "grupo38")
    SQLALCHEMY_TRACK_MODIFICATIONS = false
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", "807725485516-fcfop9t624v60qrlfoc52rulo5j953e0.apps.googleusercontent.com")
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", "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")
    GOOGLE_REDIRECT_URI = environ.get("GOOGLE_REDIRECT_URI", "https://admin-grupo38.proyecto2021.linti.unlp.edu.ar/login/callback")
    

class DevelopmentConfig(Config):
    """Development configuration."""

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = false
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_REDIRECT_URI = environ.get("GOOGLE_REDIRECT_URI", None)


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = "test"
    SQLALCHEMY_TRACK_MODIFICATIONS = false
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_REDIRECT_URI = environ.get("GOOGLE_REDIRECT_URI", None)


config = dict(
    development=DevelopmentConfig, test=TestingConfig, production=ProductionConfig
)

## More information
# https://flask.palletsprojects.com/en/2.0.x/config/
