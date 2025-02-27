from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Product
from app import db, cache

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], description=data.get('description'))
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201

@product_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
@cache.cached(timeout=300)
def read_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({"name": product.name, "price": product.price, "description": product.description})

@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.price = data['price']
    product.description = data.get('description')
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})

@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})

@product_bp.route('/', methods=['GET'])
@jwt_required()
@cache.cached(timeout=300)
def list_products():
    products = Product.query.all()
    return jsonify([{"id": product.id, "name": product.name, "price": product.price, "description": product.description} for product in products])
