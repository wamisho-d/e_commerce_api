import unittest
from unittest.mock import patch
from app import app, db
from models import Customer, Product, Order, OrderProduct
import json

class ECommerceAPITestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.drop_all()
    
    def setUp(self):
        self.client = self.__class__.client
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer <your_jwt_token_here>'
        }
    
    def test_create_customer(self):
        data = {"name": "Thomas Jack", "email": "thomas@gmail.com", "phone": "2345678909"}
        response = self.client.post('/api/customers/', data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Customer created successfully", response.get_data(as_text=True))
    
    def test_create_product(self):
        data = {"name": "Sample Product", "price": 20.98, "description": "A sample product."}
        response = self.client.post('/api/products/', data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Product created successfully", response.get_data(as_text=True))
    
    def test_place_order(self):
        with app.app_context():
            customer = Customer(name="Thomas Jack", email="thomas@gmail.com", phone="3456327654")
            product = Product(name="Another Product", price=30.89, description="Another sample product.")
            db.session.add(customer)
            db.session.add(product)
            db.session.commit()
            customer_id = customer.id
            product_id = product.id

        data = {
            "customer_id": customer_id,
            "products": [
                {"product_id": product_id, "quantity": 2}
            ]
        }
        response = self.client.post('/api/orders/', data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Order placed successfully", response.get_data(as_text=True))
    
    def test_read_customer(self):
        with app.app_context():
            customer = Customer(name="Charles", email="charles@gmail.com", phone="3224567345")
            db.session.add(customer)
            db.session.commit()
            customer_id = customer.id

        response = self.client.get(f'/api/customers/{customer_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Charles", response.get_data(as_text=True))
    
    def test_read_product(self):
        with app.app_context():
            product = Product(name="Product to Read", price=50.79, description="A product to read.")
            db.session.add(product)
            db.session.commit()
            product_id = product.id

        response = self.client.get(f'/api/products/{product_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Product to Read", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
