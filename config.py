import os

class Config(object):
    # this config variable is important to Flask applications
    # Flask uses value of secret key as a cryptographic key, useful to generate signatures or tokens

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'