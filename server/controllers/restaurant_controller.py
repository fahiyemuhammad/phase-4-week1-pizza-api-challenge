from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server import db

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
    """
    Fetch a single restaurant by ID, including its associated pizzas.
    """
    restaurant = db.session.get(Restaurant, id) 
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
    """
    Delete a restaurant and all associated restaurant_pizzas.
    """
    restaurant = db.session.get(Restaurant, id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    try:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete restaurant.'}), 500