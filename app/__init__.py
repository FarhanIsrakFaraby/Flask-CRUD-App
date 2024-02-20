from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
# from app import db

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db`'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        migrate.init_app(app, db)

        # from app import models, routes

        # from app.routes import main_bp
        # app.register_blueprint(main_bp)

        from app.api import bp as api_bp
        app.register_blueprint(api_bp, url_prefix='/api')

    return app
