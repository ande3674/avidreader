import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # this config variable is important to Flask applications
    # Flask uses value of secret key as a cryptographic key, useful to generate signatures or tokens

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    # GOOGLE API INFO
    URL_END = '&key=AIzaSyAdhqZaUyS--kQ3BnAjUOmmfSc70FeCYwg'
    URL_START = 'https://www.googleapis.com/books/v1/volumes?q='

    # NYT API INFO
    NYT_KEY = 'ffcd3be1d1eb404ba71dc5743e36ff3f'
    NYT_URL = 'https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-fiction&api-key=ffcd3be1d1eb404ba71dc5743e36ff3f'
    NYT_URL_NONFICTION = 'https://api.nytimes.com/svc/books/v3/lists.json?list=e-book-nonfiction&api-key=ffcd3be1d1eb404ba71dc5743e36ff3f'