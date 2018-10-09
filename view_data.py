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

# Print all customers
print("\nCustomers:")
for customer in session.query(Customer).all():
    print(customer)

# Print all products
print("\nProducts:")
for product in session.query(Product).all():
    print(product)

# Print all orders
print("\nOrders:")
for order in session.query(Order).all():
    print(order)