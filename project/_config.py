import os


basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = 'satfan.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SCLALCHEMY_TRACK_MODIFICATIONS = False
#URI
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

DEBUG = True
