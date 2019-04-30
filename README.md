Rest IP Address/CIDR API
===============================

version number: 1.0.0
author: Freemon Johnson

Overview
--------

Create a simple IP Address Management REST API using python on top of any data store. It will consist of the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”.
 
The REST API must support four endpoints…
                - Create IP addresses - take in a CIDR block and add all IP addresses within that block to the database with status “available”
                - List IP addresses - return all IP addresses in the system with their current status
                - Acquire an IP - set the status of a certain IP to “acquired”
                - Release an IP - set the status of a certain IP to “available”
 


Methodology
-----------
I utilized the **Flask** framework to create my 4 endpoints and services which are the following:

**POST:** http://localhost:5000/createipaddr
```
JSON{
		'id':<numeric value>
		'ip':CIDR-> "192.168.0.1" or "192.168.1.0/24"
	}
```

**GET:** http://localhost:5000/listips
```
<NO JSON PAYLOAD>
```

**PUT:** http://localhost:5000/acquireip
```
JSON{
		'id': <placholder for PRIMARY KEY>
		'ip':CIDR-> "192.168.0.1" or "192.168.1.0/24" # ip or mask you acquiring
    }
```
    
**PUT:** http://localhost:5000/releaseip
```
JSON{
		'id': <placholder for PRIMARY KEY>
		'ip':CIDR-> "192.168.0.1" or "192.168.1.0/24" # ip or mask you releasing
	}
```
Documentation is built with Sphinx.


Installation / Usage
--------------------
*Installation Requirements*: 
    * python version 3.x. 
    * postgres database
    * flask framework
    * virtualenv

*Installation Dependencies*:
	You need to know the following for your postgres database:
		- database name
		- username
		- password
		- domain name
	_Since Ntrepid uses Macs that is the platform assumption_
	There is file _setup.sh_ that will install the ruby, brew, postgres, virtualenv if needed.


**To build web based documentation:**

You need to install _sphinx_ package: [here](http://www.sphinx-doc.org/en/master/usage/installation.html)

Please edit the following files on your system after running: 
	
	$ sphinx-quickstart

**conf.py**:

	sys.path.append(<where you *.rst files are located>)
	
	I highly recommend changing the <html_theme> to "default" or "sphinx_rtd_theme"

cd into **docs** and type 

    $ sphinx-build -b html <docs directory path> <build/html directory path>


My documentation can presently be opened with a web browser at **index.html** file in _flask_api/docs/\_build/_ directory.


Example
-------

	$  python run.py
