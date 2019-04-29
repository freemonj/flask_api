'''
Created on Apr 26, 2019

@author: freemonj
'''
from flask_restful import Resource
from flask import request
from Model import db, IPAddrs, IPAddrsSchema
import traceback as tb


ipaddrs_schema = IPAddrsSchema(many=True)
ipaddr_schema = IPAddrsSchema()

class IPAddrResource(Resource):
    def get(self):
        """
        GET to return the IP address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """                
        ipaddrs = IPAddrs.query.all()
        ipaddrs = ipaddrs_schema.dump(ipaddrs).data
        return {'status': 'success', 'data': ipaddrs}, 200
    
    def post(self):
        """
        POST to create the IP Address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """
        try:                
            json_data = request.get_json(force=True)
            #json_data = json.loads(request.data, strict=False)
        except:
            print("Trace = {}".format(tb.format_exc()))
        if not json_data:
            return {'message': 'No IP address data provided'}, 400
        # Validate and deserialize input
        data, errors = ipaddr_schema.load(json_data)
        if errors:
            return errors, 422
        ipaddrs = IPAddrs.query.filter_by(ip=data['ip']).first()
        if ipaddrs:
            return {'message': 'IP already exists'}, 400
        ipaddr = IPAddrs(
            id=json_data['id'],
            ip=json_data['ip'],
            status=json_data['status']
            )

        db.session.add(ipaddr)
        db.session.commit()

        result = ipaddr_schema.dump(ipaddr).data

        return { "status": 'success', 'data': result }, 201
