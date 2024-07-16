from flask import Blueprint, request, session, make_response, jsonify
from models import db, Commodity, Category
from flask_restful import Api, Resource, reqparse


commodities_bp = Blueprint ('commodities_bp', __name__, url_prefix='/commodities')

commodities_api = Api(commodities_bp)

class GetCommodities(Resource):

    def get(self):
        commodities = [commodity.to_dict() for commodity in Commodity.query.all()]
        return commodities

commodities_api.add_resource(GetCommodities, '/all')