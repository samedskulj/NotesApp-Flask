from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "database.db"


def kreiraj_aplikaciju():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "samedovrepository"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    kreiraj_bazu_podataka(app)
    return app


def kreiraj_bazu_podataka(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Kreirana baza podataka")
