from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Validation
    if not email or not password:
        return "<script>alert('All fields are required.');window.history.back();</script>"
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "<script>alert('Enter a valid email address.');window.history.back();</script>"
    if len(password) < 6:
        return "<script>alert('Password must be at least 6 characters long.');window.history.back();</script>"

    return redirect(url_for('home'))

@app.route('/home')
def home():
    pins = [
        {"id": 1, "title": "Grilled Chicken with Garlic Butter Sauce", "image": "static/images/pin1.jpg"},
        {"id": 2, "title": "Chicken Alfredo Pasta", "image": "static/images/pin2.jpg"},
        {"id": 3, "title": "Creamy Mushroom Risotto", "image": "static/images/pin3.jpg"},
        {"id": 4, "title": "Baked Mac and Cheese", "image": "static/images/pin4.jpg"},
        {"id": 5, "title": "Classic Caesar Salad", "image": "static/images/pin5.jpg"},
        {"id": 6, "title": "Roasted Vegetable Lasagna", "image": "static/images/pin6.jpg"},
        {"id": 7, "title": "French Onion Soup", "image": "static/images/pin7.jpg"},
        {"id": 8, "title": "Garlic Butter Prawns", "image": "static/images/pin8.jpg"},
        {"id": 9, "title": "Chicken Salad", "image": "static/images/pin9.jpg"},
        {"id": 10, "title": "Margherita Pizza", "image": "static/images/pin10.jpg"},
        {"id": 11, "title": "Grilled Chicken Sandwich", "image": "static/images/pin11.jpg"},
        {"id": 12, "title": "Chicken Steak with Mashed Potatoes", "image": "static/images/pin12.jpg"}
    ]
    return render_template("home.html", pins=pins)

@app.route('/pin/<int:pin_id>')
def pin_detail(pin_id):
    pins = {
    1: {"title": "Grilled Chicken with Garlic Butter Sauce", "desc": "Juicy grilled chicken topped with rich garlic butter sauce.", "image": "static/images/pin1.jpg"},
    2: {"title": "Chicken Alfredo Pasta", "desc": "Creamy Alfredo pasta with tender chicken and parmesan.", "image": "static/images/pin2.jpg"},
    3: {"title": "Creamy Mushroom Risotto", "desc": "Classic Italian risotto cooked with mushrooms and cheese.", "image": "static/images/pin3.jpg"},
    4: {"title": "Baked Mac and Cheese", "desc": "Cheesy baked macaroni with a crispy golden topping.", "image": "static/images/pin4.jpg"},
    5: {"title": "Classic Caesar Salad", "desc": "Crisp romaine lettuce tossed with Caesar dressing and croutons.", "image": "static/images/pin5.jpg"},
    6: {"title": "Roasted Vegetable Lasagna", "desc": "Layered lasagna with roasted veggies and creamy cheese sauce.", "image": "static/images/pin6.jpg"},
    7: {"title": "French Onion Soup", "desc": "Caramelized onion soup topped with melted cheese and bread.", "image": "static/images/pin7.jpg"},
    8: {"title": "Garlic Butter Prawns", "desc": "Succulent prawns sautéed in butter, garlic, and herbs.", "image": "static/images/pin8.jpg"},
    9: {"title": "Chicken Salad", "desc": "Healthy mix of chicken, greens, and tangy dressing.", "image": "static/images/pin9.jpg"},
    10: {"title": "Margherita Pizza", "desc": "Classic pizza with mozzarella, tomatoes, and basil.", "image": "static/images/pin10.jpg"},
    11: {"title": "Grilled Chicken Sandwich", "desc": "Tender grilled chicken served in toasted bread with veggies.", "image": "static/images/pin11.jpg"},
    12: {"title": "Chicken Steak with Mashed Potatoes", "desc": "Seared chicken steak paired with creamy mashed potatoes.", "image": "static/images/pin12.jpg"},
}

    pin = pins.get(pin_id)
    return render_template("pin.html", pin=pin)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
