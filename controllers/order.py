from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Order, OrderProduct, Product
from app import db

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/', methods=['POST'])
@jwt_required()
def place_order():
    data = request.get_json()
    new_order = Order(customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()
    
    for item in data['products']:
        order_product = OrderProduct(order_id=new_order.id, product_id=item['product_id'], quantity=item['quantity'])
        db.session.add(order_product)
    
    db.session.commit()
    return jsonify({"message": "Order placed successfully"}), 201

@order_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def retrieve_order(id):
    order = Order.query.get_or_404(id)
    products = OrderProduct.query.filter_by(order_id=order.id).all()
    return jsonify({
        "order_date": order.order_date,
        "customer_id": order.customer_id,
        "products": [{"product_id": prod.product_id, "quantity": prod.quantity} for prod in products]
    })
