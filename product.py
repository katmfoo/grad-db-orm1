'''
Model for product table
Created on Oct 9, 2018 by Patrick Richeal
'''

from sqlalchemy import Column, String, Integer, Numeric, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from base import BASE

# A product can be a part of many orders, and an order may contain many products (M:M relationship)
class Product(BASE):
    __tablename__ = 'product'

    product_id = Column(Integer, nullable=False, primary_key=True)
    product_code = Column(String(10), nullable=False)
    name = Column(String(45), nullable=False)
    cost = Column(Numeric, nullable=False)
    minimum_supply_level = Column(Integer, nullable=False)
    current_supply_level = Column(Integer, nullable=False)

    orders = relationship("Order", secondary="order_product", viewonly=True)

    __table_args__ = (
       PrimaryKeyConstraint('product_id', name='PRIMARY'),
    )

    def __init__(self, product_code, name, cost, minimum_supply_level, current_supply_level):
        self.product_code = product_code
        self.name = name
        self.cost = cost
        self.minimum_supply_level = minimum_supply_level
        self.current_supply_level = current_supply_level

    def __repr__(self):
        return "{self.product_code} | {self.name} | ${self.cost}".format(self=self)