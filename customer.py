'''
Model for customer table
Created on Oct 9, 2018 by Patrick Richeal
'''

from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from base import BASE

# A customer can have many orders, but an order is only made by one customer (1:M relationship)
class Customer(BASE):
    __tablename__ = 'customer'

    customer_id = Column(Integer, nullable=False, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)

    orders = relationship("Order", viewonly=True)

    __table_args__ = (
       PrimaryKeyConstraint('customer_id', name='PRIMARY'),
    )

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "{self.customer_id} | {self.first_name} {self.last_name}".format(self=self)