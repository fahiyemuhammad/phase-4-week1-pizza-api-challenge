from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    """
    Create a new restaurant-pizza association with a given price.
    """
    data = request.get_json()

    try:
        price = float(data.get('price'))
        if price < 1 or price > 30:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    pizza = db.session.get(Pizza, pizza_id)
    restaurant = db.session.get(Restaurant, restaurant_id)

    if not pizza or not restaurant:
        return jsonify({'errors': ['Invalid pizza_id or restaurant_id']}), 400

    rp = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)

    try:
        db.session.add(rp)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['Failed to create restaurant pizza.']}), 500

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