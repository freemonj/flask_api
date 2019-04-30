'''
Created on Apr 26, 2019

@author: freemonj
'''
from flask_restful import Resource
from flask import request
from Model import db, IPAddrs, IPAddrsSchema
import traceback as tb
import ipaddress

ipaddrs_schema = IPAddrsSchema(many=True)
ipaddr_schema = IPAddrsSchema()

class IPAddrResource(Resource):
#     def get(self):
#         """
#         GET to return/list the IP address.
#         :params: None
#         :return: GET HTML code
#         :rtype: Integer
#         """                
#         ipaddrs = IPAddrs.query.all()
#         ipaddrs = ipaddrs_schema.dump(ipaddrs).data
#         return {'status': 'success', 'data': ipaddrs}, 200
    
    def _processSingleIP(self,IPAddrs,json_data):
        ipaddr = IPAddrs(
            id=json_data['id'],
            ip=json_data['ip'],
            status='available'
            )        
        return ipaddr
    
    def _processMultipleIP(self,IPAddrs,json_data,theip,id):
        ipaddr = IPAddrs(
            id=id,
            ip=str(theip),
            status='available'
            )
        return ipaddr
    
    def post(self):
        """
        POST to create the IP Address.
        :params: None
        :return: GET HTML code
        :rtype: Integer
        """
        try:                
            json_data = request.get_json(force=True)            
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
        adr = ipaddress.ip_network(json_data['ip'])
        ipl = [str(ip) for ip in adr.hosts()]
        if len(ipl) == 0:
            ipaddr = self._processSingleIP(IPAddrs,json_data)
            db.session.add(ipaddr)      
        elif len(ipl) > 0:
            #ip with mask was provided
            for ind,theip in enumerate(ipl):
                ipaddr = self._processMultipleIP(IPAddrs, json_data, theip,ind)
                db.session.add(ipaddr)      
        else:
            raise("The JSON {} provided  was formated correctly".format(json_data))
        
        db.session.commit()  
        result = ipaddr_schema.dump(ipaddr).data

        return { "status": 'success', 'data': result }, 201
