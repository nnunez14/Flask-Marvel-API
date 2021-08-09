from flask import Blueprint, request, jsonify
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db, User, Marvel, marvel_schema, marvels_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'some_value': 52, 'another_value': 800}

@api.route('/marvels', methods = ['POST'])
@token_required
def create_marvel(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    camera_quality = request.json['camera_quality']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    user_token = current_user_token.token

    print(f'TESTER: {current_user_token.token}')

    marvel = Marvel(name,description,price,camera_quality,flight_time,max_speed,dimensions,weight,cost_of_prod,series,user_token = user_token)

    db.session.add(marvel)
    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)


@api.route('/marvel', methods = ['GET'])
@token_required
def get_marvel(current_user_token):
    owner = current_user_token.token
    marvels = Marvel.query.filter_by(user_token = owner).all()
    response = marvels_schema.dump(marvels)
    return jsonify(response)


@api.route('/marvels/<id>', methods = ['GET'])
@token_required
def get_marvels(current_user_token, id):
    owner = current_user_token.token
    marvel = Marvel.query.get(id)
    response = marvel_schema.dump(marvel)
    return jsonify(response)

# UPDATE A CAR BY ID ENDPOINT
@api.route('/marvels/<id>', methods = ['POST'])
@token_required
def update_marvel(current_user_token, id):
    marvel = Marvel.query.get(id)
    print(marvel)
    marvel.name = request.json['name']
    marvel.description = request.json['description']
    marvel.price = request.json['price']
    marvel.camera_quality = request.json['camera_quality']
    marvel.flight_time = request.json['flight_time']
    marvel.max_speed = request.json['max_speed']
    marvel.dimensions = request.json['dimensions']
    marvel.weight = request.json['weight']
    marvel.cost_of_prod = request.json['cost_of_prod']
    marvel.series = request.json['series']
    marvel.user_token = current_user_token.token
    db.session.commit()

    response = marvel_schema.dump(marvel)
    return jsonify(response)


@api.route('/marvel/<id>', methods = ['DELETE'])
@token_required
def delete_marvel(current_user_token, id):
    marvel = Marvel.query.get(id)
    if marvel:
        db.session.delete(marvel)
        db.session.commit()

        response = marvel_schema.dump(marvel)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That hero does not exist!'})




