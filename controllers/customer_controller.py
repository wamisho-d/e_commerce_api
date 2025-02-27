from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Customer, CustomerAccount
from app import db

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/', methods=['POST'])
@jwt_required()
def create_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer created successfully"}), 201

@customer_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def read_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify({"name": customer.name, "email": customer.email, "phone": customer.phone})

@customer_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get_or_404(id)
    customer.name = data['name']
    customer.email = data['email']
    customer.phone = data['phone']
    db.session.commit()
    return jsonify({"message": "Customer updated successfully"})

@customer_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"})

@customer_bp.route('/accounts', methods=['POST'])
@jwt_required()
def create_customer_account():
    data = request.get_json()
    new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({"message": "Customer account created successfully"}), 201

@customer_bp.route('/accounts/<int:id>', methods=['GET'])
@jwt_required()
def read_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    customer = Customer.query.get_or_404(account.customer_id)
    return jsonify({"username": account.username, "customer": {"name": customer.name, "email": customer.email, "phone": customer.phone}})

@customer_bp.route('/accounts/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer_account(id):
    data = request.get_json()
    account = CustomerAccount.query.get_or_404(id)
    account.username = data['username']
    account.password = data['password']
    db.session.commit()
    return jsonify({"message": "Customer account updated successfully"})

@customer_bp.route('/accounts/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "Customer account deleted successfully"})
