Welcome to IP Endpoint API's documentation!
===========================================

**Rest IP Address/CIDR API**

*version number: 1.0.0*

**author: Freemon Johnson**

**Overview**

Create a simple IP Address Management REST API using python on top of any data store. It will consist of the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”.

The REST API must support four endpoints:

- Create IP addresses 
- take in a CIDR block and add all IP addresses within that block to the database with status “available” 
- return all IP addresses in the system with their current status 
- Acquire an IP -> set the status of a certain IP to “acquired” 
- Release an IP -> set the status of a certain IP to “available”

**Methodology**

I utilized the Flask framework to create my 4 endpoints and services.

**Installation/Usage**

**Installation Requirements:** 

* python version 3.x. 
* postgres database 
* flask framework 
* virtualenv

**Installation Dependencies:** 

You need to know the following for your postgres database: 

- database name 
- username 
- password 
- domain name 

Since Ntrepid uses Macs that is the platform assumption There is file setup.sh that will install the ruby, brew, postgres, virtualenv if needed.

*To build web based documentation:*

You need to install sphinx package from PyPI or brew.

Please edit the following files on your system after running:

	$ sphinx-quickstart

**conf.py:**

	```sys.path.append(<where you *.rst files are located>)```

	I highly recommend changing the <html_theme> to "default" or "sphinx_rtd_theme"

*$ sphinx-build -b html <docs directory path> <build/html directory path>*

**My documentation can presently be opened with a web browser at index.html file in "flask_api/_build/html/index.html" directory.**

Example

$  python src/run.py

.. automodule:: src.run
   :members:

.. automodule:: src.Model
   :members:

.. automodule:: src.resources.acquire
   :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
