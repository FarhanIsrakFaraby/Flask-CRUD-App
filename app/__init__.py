# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from .config import Config
from . import mysql

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     migrate.init_app(app, db)

#     from app.models.user import User
#     from app.routes.user_routes import user_routes

#     app.register_blueprint(user_routes)

#     return app

from flask import Flask
from flask_mysqldb import MySQL
from .routes.user_routes import user_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # MySQL configuration
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flaskdb' # Updated database name
    # app.config['MYSQL_SOCKET'] = '/var/run/mysqld/mysqld.sock'
    app.config['MYSQL_PORT'] = 3306 
    mysql = MySQL(app)

    # Register blueprints
    app.register_blueprint(user_routes)

    return app

