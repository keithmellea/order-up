import os


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
