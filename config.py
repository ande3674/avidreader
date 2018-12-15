import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # this config variable is important to Flask applications
    # Flask uses value of secret key as a cryptographic key, useful to generate signatures or tokens

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3