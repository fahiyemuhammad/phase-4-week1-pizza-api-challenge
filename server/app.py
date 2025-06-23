from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import validates


db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza



# from server.controllers.pizza_controller import pizza_bp
# from server.controllers.restaurant_controller import restaurant_bp
# from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

#pizza controller
pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [
        {'id': p.id, 'name': p.name, 'ingredients': p.ingredients}
        for p in pizzas
    ]
    return jsonify(result), 200

#restaurant-pizza controller
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not price or price < 1 or price > 30:
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({'errors': ['Invalid pizza_id or restaurant_id']}), 400

    rp = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)

    db.session.add(rp)
    db.session.commit()

    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': pizza.id,
        'restaurant_id': restaurant.id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201
#restaurant controller

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [
        {'id': r.id, 'name': r.name, 'address': r.address}
        for r in restaurants
    ]
    return jsonify(result), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [
            {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            } for rp in restaurant.restaurant_pizzas
        ]
    }), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204


app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def index():
    return {'message': 'Pizza API is running!'}