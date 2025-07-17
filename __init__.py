from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'your_seret_key'
    app.config['SQLALCHEMY_DATABASE-URI'] = 'sqllite:///todo.db'
    app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False

    db._init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app