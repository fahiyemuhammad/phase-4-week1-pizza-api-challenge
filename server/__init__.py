from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Registering blueprints
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
    
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route('/')
    def index():
        return {'message': 'Pizza API is running!'}

    return app

__all__ = ['create_app']
