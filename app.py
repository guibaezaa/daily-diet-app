from flask import Flask, request, jsonify
from database import db
from models.meal import Meal
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily_diet.db'

db.init_app(app)

@app.route('/meals', methods=['POST'])
def add_meal():
    data = request.get_json()
    new_meal = Meal(
        name=data['name'],
        description=data.get('description'),
        diet=data['diet'],
        insert_timestamp=datetime.utcnow()
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({"message": "Meal added successfully"}), 201

@app.route('/meals', methods=['GET'])
def get_meals():
    meals = Meal.query.all()
    return jsonify([meal.to_dict() for meal in meals]), 200

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    if meal is None or meal.id != meal_id:
        return jsonify({"error": "Meal not found"}), 404
    return jsonify(meal.to_dict()), 200

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    data = request.get_json()
    meal.name = data.get('name', meal.name)
    meal.description = data.get('description', meal.description)
    meal.diet = data.get('diet', meal.diet)
    db.session.commit()
    if meal is None or meal.id != meal_id:
        return jsonify({"error": "Meal not found"}), 404
    return jsonify({"message": "Meal updated successfully"}), 200

@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": "Meal deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)