'''
Created on Apr 27, 2019

@author: freemonj
'''
from flask import request
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema

availabilities_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()
ipaddrs_schema = IPAddrsSchema(many=True)
ipaddr_schema = IPAddrsSchema()

class ReleaseResource(Resource):
    
    def _processSingleIP(self,ipaddrs,json_data):
        for jblk in ipaddrs:
            if jblk['ip'] == json_data['ip']:
                jblk['status'] = 'available'
                break
        return ipaddrs
        
    def _processMultipleIP(self,IPAddrs,json_data,theip,id):
        for theip in ipl:
            for jblk in ipaddrs['data'].items():
                if jblk['ip'] == theip:
                    jblk['status'] = 'available'
                    break
        return ipaddrs
        
    def put(self):
        """
        PUT to release to make IP available CIDR/IP Address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """             
        json_data = request.get_json(force=True)
        ipaddrs = IPAddrs.query.all()
        ipaddrs = ipaddrs_schema.dump(ipaddrs).data 
        
        if not json_data:
            return {'message': 'CIDR availability does not exist'}, 400
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return errors, 422
        adr = ipaddress.ip_network(json_data['ip'])
        ipl = [str(ip) for ip in adr.hosts()]
        if len(ipl) == 0:
            ipaddr = self._processSingleIP(ipaddrs, json_data)
            db.session.add(ipaddrs_schema.dump(ipaddr).data)            
        elif len(ipl) > 0:
            ipaddr = self._processMultipleIP(IPAddrs, json_data, theip, id)
            db.session.add(ipaddrs_schema.dump(ipaddr).data)
                

        db.session.commit()
        result = availabilities_schema.dump(ipaddr).data

        return { "status": 'success', 'data': result }, 204