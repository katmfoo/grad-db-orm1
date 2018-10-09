'''
Inserts data into the database
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

# Make a new customer
customer = Customer('Patrick', 'Richeal')

# Make a new order
order = Order(customer)

session.add(order)
session.commit()

product = Product(
    'ND928AMP10',
    'Yamaha Digital Piano',
    1299.99,
    10,
    24
)

order.addProduct(product)

session.commit()