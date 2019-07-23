from flask import Flask
from config import HOST
# from flask_sqlalchemy import get_debug_queries

from flask_sqlalchemy import get_debug_queries

# from version import *
from routes.usersroute import usersapi

app = Flask(__name__)
api_version = '/api/v1.0'

"""
Blueprint is structuring the api's
"""

app.register_blueprint(usersapi, url_prefix=api_version)





if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST['HOST'], port=HOST['PORT'])
