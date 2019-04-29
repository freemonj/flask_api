'''
Created on Apr 27, 2019

@author: freemonj
'''
from flask import request
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema

availabilities_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()

class AvailabilityResource(Resource):
    def get(self):
        """
        GET to return the availability of the CIDR/IP Address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """                
        availabilities = Availability.query.all()
        availabilities = availabilties_schema.dump(availabilities).data
        return {'status': 'success', 'data': availabilities}, 200
    
#     def post(self):
#         """
#         POST to acquire IP CIDR/IP Address.
#         :params: None
#         :return: GET HTML code
#         :rtype: Integer
#         """             
#         json_data = request.get_json(force=True)
#         if not json_data:
#             return {'message': 'No input data provided'}, 400
#         # Validate and deserialize input
#         data, errors = availabilites_schema.load(json_data)
#         if errors:
#             return errors, 422
#         availability = Availability.query.filter_by(ready=data['ready']).first()
#         availability = Availability(
#             ready=json_data['ready']
#             )
# 
#         db.session.add(availability)
#         db.session.commit()
# 
#         result = availabilities_schema.dump(availability).data
# 
#         return { "status": 'success', 'data': result }, 201
    
    def put(self):
        """
        PUT to update/acquire the availability of the CIDR/IP Address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """             
        #json_data = request.get_json(force=True)
        availabilities = Availability.query.all()
        availabilities = availabilties_schema.dump(availabilities).data        
        if not json_data:
            return {'message': 'CIDR availability does not exist'}, 400
        # Validate and deserialize input
        data, errors = availabilities_schema.load(json_data)
        if errors:
            return errors, 422
        availability = Availability.query.filter_by(id=data['id']).first()
        for jblk in availabilities['data'].items():
            if jblk['ip'] == data['ip']:
                jblk['status'] = 'available'
                break

        db.session.commit()
        result = availabilities_schema.dump(availability).data

        return { "status": 'success', 'data': result }, 204