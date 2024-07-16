from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()

# Association table for many-to-many relationship between Cart and Commodity
cart_items = db.Table('cart_items',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),
    db.Column('commodity_id', db.Integer, db.ForeignKey('commodity.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False, default=1)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    carts = db.relationship('Cart', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    commodities = db.relationship('Commodity', backref='category', lazy=True)

class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    reviews = db.relationship('Review', backref='commodity', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)

    @hybrid_property
    def total(self):
        return sum(item.quantity * item.commodity.price for item in self.items)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    commodity_id = db.Column(db.Integer, db.ForeignKey('commodity.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    commodity = db.relationship('Commodity', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    commodity_id = db.Column(db.Integer, db.ForeignKey('commodity.id'), nullable=False)
