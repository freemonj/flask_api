from flask import Blueprint
from flask_restful import Api
from resources.ipaddrs import IPAddrResource
from resources.acquire import AcquireResource
from resources.release import ReleaseResource
from resources.listaddrs import IPListAddrResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
'''
ENDPOINT routes for API
'''
api.add_resource(IPAddrResource, '/createipaddr')
api.add_resource(IPListAddrResource, '/listips')
api.add_resource(AcquireResource, '/acquireip')
api.add_resource(ReleaseResource, '/releaseip')