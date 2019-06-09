# services/users/project/__init__.py

import os  # nuevo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # nuevo
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS  # nuevo

# instanciando la db
db = SQLAlchemy()  # nuevo
toolbar = DebugToolbarExtension()  # nuevo
cors = CORS() # nuevo


# nuevo
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # estableciendo configuracion
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # configurando extensiones
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app) #nuevo

    # registro blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # contexto de shell for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
