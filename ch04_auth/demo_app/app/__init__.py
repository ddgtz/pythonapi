from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_mgr = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('ch04_auth.demo_app.app.config.Config')

    db.init_app(app)
    login_mgr.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        db.create_all()

    return app
