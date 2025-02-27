from flask import Flask
from controllers.customer_controller import customer_bp
from controllers.product_controller import product_bp
from controllers.order_controller import order_bp

def register_routes(app: Flask):
    app.register_blueprint(customer_bp, url_prefix='/api/customers')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
