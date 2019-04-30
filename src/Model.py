'''
Created on Apr 26, 2019

@author: freemonj
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()



class IPAddrs(db.Model):
    '''
    IP Address class model
    '''
    __tablename__ = 'ipaddrs'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    #creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    #ip_id = db.Column(db.Integer, db.ForeignKey('cidr.id', ondelete='CASCADE'), nullable=True)
    #availability = db.relationship('CIDRBlock', backref=db.backref('ipaddress', lazy='dynamic' ))

    def __init__(self, id, ip, status):
        self.id = id
        self.ip = ip
        self.status = status

class IPAddrsSchema(ma.Schema):
    '''
    IP Address Schema for JSON data
    '''    
    id = fields.Integer()
    ip = fields.String(required=True)
    status = fields.String(required=True)


class Availability(db.Model):
    '''
    Availability class model for CIDR/IPs
    '''
    __tablename__ = 'availability'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(150), unique=False, nullable=False)

    def __init__(self,id, ip):
        self.ip = ip
        self.id = id


class AvailabilitySchema(ma.Schema):
    '''
    Availability Schema for JSON data
    '''
    id = fields.Integer()
    ip = fields.String(required=True)




