import os
import getpass

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
username = input('Username: ')
database_name = input('Database Name: ')
password = getpass.getpass(prompt='Password: ', stream=None)
domainname = input('DomainName or Default = localhost by pressing <Enter>: ')
if domainname == "":
    domainname = 'localhost'
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(username,password,domainname,database_name)