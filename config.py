import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.getenv(
        "DEVELOPMENT_DATABASE_URL"))
    JWT_SECRET_KEY = 'jwt-secret-key'
    JWT_TOKEN_LOCATION = ['headers']
