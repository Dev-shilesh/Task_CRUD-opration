from flask import Blueprint, request, jsonify
from .model import User
from . import db

routes = Blueprint("route", __name__)

# create new user
@routes.route("/create_user",methods=["POST"])
def create_user():
    try:
        data = request.json
        
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        email = data.get('email')
        
        user = User(firstName=firstName,lastName=lastName,email=email)
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            "message": "User created successfully",
            "user": {
                "id" : user.id,
                "firstName" : user.firstName,
                "lastName" : user.lastName,
                "email" : user.email
            }
            }), 201

    except Exception as e:
        return {"error": str(e)}, 500
        

# get all users 
@routes.route('/get_users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    except Exception as e:
        return {"error": str(e)}, 500

# get one user 
@routes.route('/get_user/<int:id>', methods=['GET'])
def get_one_user(id):
    try:
        user = User.query.get_or_404(id)
        return jsonify(user.to_dict())

    except Exception as e:
        return {"error": str(e)}, 500

# update user
@routes.route('/update_user/<int:id>',methods=['PUT'])
def update_user(id):
    try:
        data = request.json
        
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        email = data.get('email')
        
        user = User.query.get_or_404(id)
        
        user.firstName = firstName
        user.lastName = lastName
        user.email = email
        
        db.session.commit()
        
        return jsonify({
            "message": "User updated successfully",
            "user": {
                "id" : user.id,
                "firstName" : user.firstName,
                "lastName" : user.lastName,
                "email" : user.email
            }
            }), 201

    except Exception as e:        
        return {"error": str(e)}, 500

# delete user
@routes.route('/delete_user/<int:id>',methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    except Exception as e:
        return {"error": str(e)}, 500

# delete all users