# server/controllers/restaurant_pizza_controller.py
from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.app import db

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