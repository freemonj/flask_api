from flask import request
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema,IPAddrs,IPAddrsSchema
import ipaddress

availabilities_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()
ipaddrs_schema = IPAddrsSchema(many=True)
ipaddr_schema = IPAddrsSchema()

class AcquireResource(Resource):
    '''
    Class for acquiring IP's
    '''

    def _processSingleIP(self,ipaddrs,json_data):
        for jblk in ipaddrs:
            if jblk['ip'] == json_data['ip']:
                jblk['status'] = 'acquired'
                ipaddr = IPAddrs(
                    id=jblk['id'],
                    ip=jblk['ip'],
                    status='acquired'
                    )   
                break
        return ipaddr
        
    def _processMultipleIP(self,ipl,ipaddrs):
        for obj in ipaddrs:
            if obj['ip'] in ipl:
                ipaddr = IPAddrs(
                    id=obj['id'],
                    ip=obj['ip'],
                    status='acquired'
                    )                       
                db.session.merge(ipaddr)
        return
    
    
    def put(self):
        """
        PUT to update/acquire the ip of the CIDR/IP Address.
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
            db.session.merge(ipaddr)
        elif len(ipl) > 0:
            ipaddr = self._processMultipleIP(ipl,ipaddrs)
            
        
        db.session.commit()
        result = ipaddr_schema.dump(ipaddr).data

        return { "status": 'success', 'data': result }, 204