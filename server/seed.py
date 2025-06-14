from app import app, db
from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Seeding database...")

    #clearing the table first
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    #Create pizza
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    pizza3 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Ham, Pineapple")

    #Create restaurants
    r1 = Restaurant(name="Mama Mia's", address="123 Flavor St")
    r2 = Restaurant(name="Pizza Planet", address="42 Galactic Way")

    #Add and commit pizzas and restaurants
    db.session.add_all([pizza1, pizza2, pizza3, r1, r2])
    db.session.commit()

    #Create restaurant-pizza relationships
    rp1 = RestaurantPizza(price=12.5, restaurant=r1, pizza=pizza1)
    rp2 = RestaurantPizza(price=15.0, restaurant=r1, pizza=pizza2)
    rp3 = RestaurantPizza(price=10.0, restaurant=r2, pizza=pizza3)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
