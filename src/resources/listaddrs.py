from flask_restful import Resource
from flask import request
from Model import db, IPAddrs, IPAddrsSchema
import traceback as tb
import ipaddress
import uuid

ipaddrs_schema = IPAddrsSchema(many=True)
ipaddr_schema = IPAddrsSchema()

class IPListAddrResource(Resource):
    def get(self):
        """
        GET to return/list the IP address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """                
        ipaddrs = IPAddrs.query.all()
        ipaddrs = ipaddrs_schema.dump(ipaddrs).data
        return {'status': 'success', 'data': ipaddrs}, 200
    
