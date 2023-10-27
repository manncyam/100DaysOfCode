from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random_coffee():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    coffee: Cafe = random.choice(result)
    return jsonify(cafe={
        'can_take_calls': coffee.can_take_calls,
        'coffee_price': coffee.coffee_price,
        'name': coffee.name
    })

@app.route('/all')
def get_all():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafe=[row.to_dict() for row in result])

@app.route('/search')
def search():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location==location)).scalars().all()
    if len(result) > 0:
        return jsonify(cafe=[row.to_dict() for row in result])
    return jsonify(error={location: "Sorry, we don't have a cafe at that location"})

## HTTP POST - Create Record
@app.route('/cafe/add', methods=['POST'])
def add_cafe():
    cafe = Cafe(
        name=request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price'),
    )
    with app.app_context():
        db.session.add(cafe)
        db.session.commit()

    return jsonify(response={
        "success": "Successfully added the new cafe."
    })
## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    with app.app_context():
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            cafe.coffee_price = request.args.get('new_price')
            db.session.commit()
            return jsonify({"success": "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == "TopSecretAPIKey":
        with app.app_context():
            cafe = db.session.get(Cafe, cafe_id)
            if cafe:
                db.session.delete()
                db.session.commit()
                return jsonify({"success": "Successfully delete the cafe."})
            else:
                return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})

if __name__ == '__main__':
    app.run(debug=True)
