from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def index():
    return {'message': 'Pizza API is running!'}



from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza