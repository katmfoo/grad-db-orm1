'''
Model for order and order_product table
Created on Oct 9, 2018 by Patrick Richeal
'''

import datetime
from sqlalchemy import Column, String, Integer, DateTime, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import BASE

# An order is only made by one customer, but a customer can have many orders (1:M relationship)
# An order may contain many products, and a product can be a part of many orders (M:M relationship)
class Order(BASE):
    __tablename__ = 'order'

    order_id = Column(Integer, nullable=False, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    paid_date = Column(DateTime, nullable=True)
    shipped_date = Column(DateTime, nullable=True)

    customer = relationship('Customer', backref=backref('order'))
    products = relationship('Product', secondary="order_product", viewonly=True)

    __table_args__ = (
       PrimaryKeyConstraint('order_id', name='PRIMARY'),
    )

    def __init__(self, customer):
        self.customer = customer

    def addProduct(self, product):
        self.order_product.append(Order_Product(order=self, product=product))

    def __repr__(self):
        product_string = ""
        for product in self.products:
            product_string += "\t\t" + str(product) + "\n"

        return "Order #{self.order_id}, made by {self.customer.first_name} {self.customer.last_name}\n".format(self=self) + "\tProducts within order:\n" + product_string

class Order_Product(BASE):
    __tablename__ = 'order_product'

    order_id = Column(Integer, ForeignKey('order.order_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id'), nullable=False)

    order = relationship("Order", backref=backref("order_product"))
    product = relationship("Product", backref=backref("order_product"))

    __table_args__ = (
        PrimaryKeyConstraint('order_id', 'product_id', name='PRIMARY'),
    )

    def __init__(self, order, product):
        self.order = order
        self.product = product