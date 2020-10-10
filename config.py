import os.path

basedir = os.path.abspath(os.path.dirname(__name__))

DEBUG = True
ENV = "development"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "storage.db")
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "sei-la-teste"
