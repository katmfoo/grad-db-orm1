'''
Flask server functions
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

from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = '1234567890'

@app.route("/")
def mainPage():
    return render_template('main.html')

@app.route("/customers")
def getCustomers():
    customers = session.query(Customer).all()
    return render_template('customers.html', customers = customers)

@app.route("/customers/<int:customerID>")
def getCustomer(customerID):
    customer = session.query(Customer).filter_by(customer_id = customerID).one()
    return render_template('customer.html', customer = customer)

@app.route('/customers/new/', methods=['GET','POST'])
def insertCustomer():
    if request.method == 'POST':
        session.add(Customer(request.form['first_name'], request.form['last_name']))
        session.commit()
        flash('Customer added successfully')
        return redirect(url_for('getCustomers'))
    else:
        return render_template('new_customer.html')

@app.route("/products")
def getProducts():
    products = session.query(Product).all()
    return render_template('products.html', products = products)

@app.route("/products/<int:productID>")
def getProduct(productID):
    product = session.query(Product).filter_by(product_id = productID).one()
    return render_template('product.html', product = product)

@app.route('/products/new/', methods=['GET','POST'])
def insertProduct():
    if request.method == 'POST':
        session.add(Product(request.form['product_code'], request.form['name'], request.form['cost'], request.form['minimum_supply_level'], request.form['current_supply_level']))
        session.commit()
        flash('Product added successfully')
        return redirect(url_for('getProducts'))
    else:
        return render_template('new_product.html')

@app.route("/orders")
def getOrders():
    orders = session.query(Order).all()
    return render_template('orders.html', orders = orders)

@app.route("/orders/<int:orderID>")
def getOrder(orderID):
    order = session.query(Order).filter_by(order_id = orderID).one()
    return render_template('order.html', order = order)