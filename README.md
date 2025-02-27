Advanced E-commerce API

Advanced E-commerce API Features:

  - Customer and CustomerAccount:
      - Create Customer
      - Read Customer
      - Update Customer
      - Delete Customer
      - Create CustomerAccount
      - Read CustomerAccount
      - Update CustomerAccount
      - Delete CustomerAccount

  - Product Catalog:
      - Create Product
      - Read Product
      - Update Product
      - Delete Product
      - List Products

  - Order Processing:
      - Place Order
      - Retrieve Order

Database Integration

Modularization code

Performance improvement with cache and limit implementation

Implement JWT Security

Unit test implementation with unittest

Document API with Swagger library

API Endpoints:
   - Customer Endpoints
      - POST /api/customers/ 
      -  GET /api/customers/{id} 
      -  PUT /api/customers/{id} 
      -  DELETE /api/customers/{id} 

   - Customer Account Endpoints
      -  POST /api/customers/accounts 
      -  GET /api/customers/accounts/{id}
      -  PUT /api/customers/accounts/{id} 
      -  DELETE /api/customers/accounts/{id} 

   - Product Endpoints
      - POST /api/products/ 
      - GET /api/products/{id} 
      -  PUT /api/products/{id} 
      -  DELETE /api/products/{id}
      -  GET /api/products/ 

  - Order Endpoints

      -  POST /api/orders/
      -  GET /api/orders/{id} 


Folder Structure
e_commerce_api/
├── app.py
├── config.yaml
├── models.py
├── routes.py
├── controllers/
│   ├── __init__.py
│   ├── customer_controller.py
│   ├── product_controller.py
│   ├── order_controller.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
├── requirements.txt
├── swagger.yaml

Technologies Used

  - Python
  - Flask
  - Flask-SQLAlchemy
  - Flask-JWT-Extended
  - Flask-Caching
  - Flask-Limiter
  - PyMySQL
  - PyYAML
  - Swagger   

Setup and Installation

  - Clone the repository:
      - git clone https://github.com/wamisho-d/ecommerce_api.git
      - cd ecommerce_api

  -  Create and activate a virtual environment:
      - python3 -m venv venv
      - source venv/bin/activate   # On Windows use `venv\Scripts\activate`

  - Install the required packages:
      - pip install -r requirements.txt
  
  - Configure the database:
      - Update the config.yaml file with your MySQL database credentials.
      - Create the database schema:

        from app import db
        db.create_all()

  - Run the application:
      - python app.py

  - Access the API documentation:
      - Open your browser and navigate to http://localhost:5000/swagger.

Running Tests
  - To run the unit tests, use the following command:

      - python -m unittest discover -s tests


Contributing

Contributions to enhance this application are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Support

If you encounter any issues, please open a problem on the project's GitHub page.

Author info

Wamisho Debero - [wamisho-d/Advanced E-commerce API ]https://github.com/wamisho-d/e_commerce_api/edit/main/README.md
