'''
Created on Apr 26, 2019

@author: freemonj
'''
from flask import Blueprint
from flask_restful import Api
from resources.ipaddrs import IPAddrResource
from resources.cidrblock import CIDRResource
from resources.availability import AvailabilityResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(IPAddrResource, '/ipaddrs')
api.add_resource(CIDRResource, '/cidrblock')
api.add_resource(AvailabilityResource, '/availability')
