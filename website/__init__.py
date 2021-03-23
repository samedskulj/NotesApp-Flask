from flask import Flask


def kreiraj_aplikaciju():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "samedovrepository"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
