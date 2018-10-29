'''
Views the data currently in the database
Created on Oct 9, 2018 by Patrick Richeal
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import BASE
from customer import Customer
from product import Product
from order import Order

# Create connection and session
connection = create_engine('mysql+pymysql://root:@localhost:3306/graddb_orm1')
BASE.metadata.create_all(connection)
Session = sessionmaker(bind=connection)
session = Session()

# Flask code

from flask import Flask
app = Flask(__name__)

@app.route("/")
def mainPage():
    return """
            <a href='customers'>View Customers</a>
            <br>
            <a href='products'>View Products</a>
            <br>
            <a href='orders'>View Orders</a>
           """

@app.route("/customers")
def getCustomers():
    output = ""
    for customer in session.query(Customer).all():
        output += str(customer) + "\n"
    return output

@app.route("/products")
def getProducts():
    output = ""
    for product in session.query(Product).all():
        output += str(product) + "\n"
    return output

@app.route("/orders")
def getOrders():
    output = ""
    for order in session.query(Order).all():
        output += str(order) + "\n"
    return output