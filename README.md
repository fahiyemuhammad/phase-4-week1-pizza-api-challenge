# 🍕 Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their prices. This project was built using **Flask**, **SQLAlchemy**, and **Flask-Migrate**, following the MVC (Model-View-Controller) architecture.

## 🚀 Features

- View all restaurants
- View a single restaurant and its pizzas
- Delete a restaurant
- View all pizzas
- Add a pizza to a restaurant with a price

## 🛠 Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (as the database)
- Postman (for testing)

## 📁 Project Structure

.
├── server/
│ ├── app.py
│ ├── config.py
│ ├── models/
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ └── controllers/
│ ├── pizza_controller.py
│ ├── restaurant_controller.py
│ └── restaurant_pizza_controller.py
└── README.md

bash
Copy
Edit

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone
   cd phase-4-week1-pizza-api-challenge
   Create and activate a virtual environment
   ```

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database (optional: you can use a script or manually add data in Flask shell)

Run the server

bash
Copy
Edit
export FLASK_APP=server.app
flask run
📬 API Endpoints
Method Endpoint Description
GET /restaurants Get all restaurants
GET /restaurants/<id> Get one restaurant with its pizzas
DELETE /restaurants/<id> Delete a restaurant
GET /pizzas Get all pizzas
POST /restaurant_pizzas Add a pizza to a restaurant

Example POST /restaurant_pizzas
json
Copy
Edit
{
"price": 15,
"pizza_id": 1,
"restaurant_id": 2
}
Expected Response
json
Copy
Edit
{
"id": 5,
"price": 15,
"pizza_id": 1,
"restaurant_id": 2,
"pizza": {
"id": 1,
"name": "Margherita",
"ingredients": "Tomato, Mozzarella, Basil"
},
"restaurant": {
"id": 2,
"name": "Mama's Pizza",
"address": "456 Cheese St"
}
}
🧪 Testing
Open Postman

Import the collection: challenge-1-pizzas.postman_collection.json

Run the included requests against http://localhost:5000

📌 Notes
Price for a pizza must be between 1 and 30

Relationships and validations are handled via SQLAlchemy models
