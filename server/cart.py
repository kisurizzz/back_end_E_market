from flask import Blueprint, request, session, make_response, jsonify
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from models import db, Cart, CartItem, User, Commodity
from flask_restful import Api, Resource, reqparse


cart_bp = Blueprint('cart_bp', __name__, url_prefix='/cart')
cart_api = Api(cart_bp)

class GetCart(Resource):

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        cart = Cart.query.filter_by(user_id = user_id).first()
        if not cart:
            return {"msg":'Cart is empty'}, 404

        return cart.to_dict(), 200

class AddToCart(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        commodity_id = data.get('commodity_id')
        quantity = data.get('quantity', 1)

        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            db.session.add(cart)
            db.session.commit()

        cart_item = CartItem.query.filter_by(cart_id=cart.id, commodity_id=commodity_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            new_item = CartItem(cart_id=cart.id, commodity_id=commodity_id, quantity=quantity)
            db.session.add(new_item)

        db.session.commit()
        return {"msg": "Item added to cart"}, 201



cart_api.add_resource(AddToCart, '/add')
cart_api.add_resource(GetCart, '/')




