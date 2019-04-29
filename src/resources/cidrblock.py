'''
Created on Apr 27, 2019

@author: freemonj
'''
from flask import request
from flask_restful import Resource
from Model import db, CIDRBlock, CIDRBlockSchema
import ipaddress

cidr_schema = CIDRBlockSchema(many=True)
cidrs_schema = CIDRBlockSchema()

class CIDRResource(Resource):
    def get(self):
        """
        GET to return the CIDR Block.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """        
        cidrs = CIDRBlock.query.all()
        cidrs = cidr_schema.dump(cidrs).data
        return {'status': 'success', 'data': cidrs}, 200
    
    def post(self):
        """
        POST to create the CIDR Block.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """        

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = cidrs_schema.load(json_data)
        if errors:
            return errors, 422
        cidrs = CIDRBlock.query.filter_by(cidr=data['cidr']).first()
        if cidrs:
            return {'message': 'CIDR block already exists'}, 400
        cidrs = CIDRBlock(
            id=json_data['id'],
            cidr=json_data['cidr'],
            status=json_data['status']
            )

        db.session.add(cidrs)
        db.session.commit()

        result = cidrs_schema.dump(cidrs).data

        return { "status": 'success', 'data': result }, 201
