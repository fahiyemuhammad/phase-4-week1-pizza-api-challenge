from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Create app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the extensions with the app
db.init_app(app)
migrate.init_app(app, db)

# Import models here so they are registered before migrations
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

# Import and register blueprints
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def index():
    return {'message': 'Pizza API is running!'}