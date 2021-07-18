from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from src import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models.modelos import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .routes.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .routes.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404