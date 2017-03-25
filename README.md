# Cash Box
Module of Cash Box realized in Odoo 10. 
#We will install odoo in linux.
__Must be installed postgresql__

    $ sudo apt-get install postgresql
    
 
___Change the permissions of postgresql:___
    We edit the configuration file of postgresql

    $   
 
___Easy way:___

For Odoo employees
------------------

To add the odoo-dev remote use this command:

    $ ./setup/setup_dev.py setup_git_dev

To fetch odoo merge pull requests refs use this command:

    $ ./setup/setup_dev.py setup_git_review
    
___way hard.___

***Step 1:***
A new user is created for odoo with all the privileges.

    $ useradd -m -g sudo -s /bin/bash new-user
***Step 2:***
Change password to new-user.
    
    $ passwd new-user
    
***Step 3:***
Update system

    $sudo apt-get update && apt-get upgrade
     
***Step 4:***
Install dependency of python
    
    $ sudo apt-get install python-virtualenv bzr bzrtools python python-egenix-mxdatetime python-dateutil python-pybabel python-openid python-feedparser python-lxml python-libxml2 python-libxslt1 python-psycopg2 python-libxml2 python-libxslt1 python-imaging python-gdata python-ldap python-reportlab python-pyparsing python-simplejson python-pydot python-webdav graphviz python-werkzeug python-matplotlib python-vatnumber python-numpy python-pychart python-vobject python-zsi python-xlwt python-hippocanvas python-profiler python-dev python-setuptools postgresql postgresql-client-common python-yaml python-mako gcc mc python-babel python-feedparser python-reportlab-accel python-zsi python-openssl python-jinja2 python-unittest2 python-mock  python-docutils lptools make python-psutil python-paramiko poppler-utils python-pdftools antiword python-jinja2 python-requests git-core sudo python-decorator python-pypdf python-passlib xsltproc xmlstarlet python-soappy python-qrencode
    
    
