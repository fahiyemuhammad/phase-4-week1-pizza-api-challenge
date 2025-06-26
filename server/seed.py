from . import db
from app import app
from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Seeding database...")

    # Clear old data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create Pizzas
    margherita = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pepperoni = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    veggie = Pizza(name="Veggie", ingredients="Tomato, Mozzarella, Peppers, Olives, Onion")

    db.session.add_all([margherita, pepperoni, veggie])
    db.session.commit()

    # Create Restaurants
    dominos = Restaurant(name="Domino's", address="123 Pizza St")
    pizza_hut = Restaurant(name="Pizza Hut", address="456 Cheesy Ave")

    db.session.add_all([dominos, pizza_hut])
    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=12.99, pizza=margherita, restaurant=dominos)
    rp2 = RestaurantPizza(price=14.99, pizza=pepperoni, restaurant=dominos)
    rp3 = RestaurantPizza(price=11.50, pizza=veggie, restaurant=pizza_hut)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print(" Done seeding!")