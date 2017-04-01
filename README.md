# Cash Box
Module of Cash Box realized in Odoo 10. 



___Easy way:___

For Odoo employees
------------------

To add the odoo-dev remote use this command:

    $ ./setup/setup_dev.py setup_git_dev

To fetch odoo merge pull requests refs use this command:

    $ ./setup/setup_dev.py setup_git_review

Install dependences for odoo

    $ ./setup/setup_dev.py setup_deps


#We will install odoo in linux.
__Must be installed postgresql__

    $ sudo apt-get install postgresql
    
 
___Change the permissions of postgresql:___
    We edit the configuration file of postgresql pg_hba.conf

    $   sudo nano /etc/postgresql/9.3/main/pg_hba.conf 
    
___Access the user su___
    
    $ sudo su
    
___change password default of postgresql___

    $ ALTER USER postgresql with passwird 'MyNewPassword';
    
    
___We logged in as user postgresql to create user su postgresql___


___we create user odoo in postgresql to work whit DB of odoo___

    $ createuser -d -S -w -R odoo
    
___Restart Service of postgresql___

    $ sudo service postgresql restart
    
    
    
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
    

    
___Update Packages of pip___

    $ pip install --upgrade pip
    
    
Odoo has many dependencies so it is recommended to install a virtual environment where we will have running our server

___Install virtualenv. It will be our virtual envirioment___

    $ virtualenv Name-our-Virtual-Envirioment

___We Activate virtual envirioment___

    $ . NameOurVirtualEnvirioment/bin/activate
    
Now we install the dependencies that are in the file requeriment.txt
 
 ___pip install -r requeriment.txt___
 
 Once finished successfully the installation, let's run the server.
 
    $ ./odoo-bin -d <namedb>
    
checked in brower.

    http://localhost:8069
    
If we have an error creating the DB, we given permission to the folder located in  ~/.local/share/Odoo

    $ sudo chown -R YouNameUser: ~/.local/share/Odoo
    

#Create Module of Odoo#

we created a folder where we will have our modules
    
    $ sudo mkdir modulos_locales
    

To create a new module we place in the folder of odoo and execute the following command

    $ ./odoo-bin scaffold <nameModuleCreated> <foldertheyoumodules>
    
Register your local module folder in odoo.

    $ ./odoo-bin -d odoo --addons-path='addons,odoo/addons,local_addons' --save
    
 ___--save: Save the configuration to a file located in ~/.odoorc where are all the configurations of the server___
    
 ___So I do not have to add the command --addons-path, For the server Read the local modules, now to run the server will only be placed the command ./odoo-bin -d <DB>___

Update change made in a module specific

    $ ./odoo-bin -d <naameBD> -u <NameOfModule>
    


***Activate developer mode on the "configuration" page of odoo***

___1. Click in tab (Configuration) or (settings) in the top of the page___
___2.Click in (Activate the developer mode) located in the down of the page)___

***Update list of application or modules of the interface of odoo***

___1. Click in (update list of application) located in the left sidebar___
___2. Click in (Applicate update)___
___Search the module create___




#How translate one module to any other idiom

___./odoo-bin -d odoo --modules=Namemodule -l es_VE --i18n-export=es_VE.po___

___--load-language = Language to load Specifies the languages ​​for the translations you want to be loaded___

___l IDIOMA, --language = (IDIOM) Specify the language of the translation file. Use it with -i18n-export o -i18n-import___
 
___--i18n-export = (Filename.extension) Export all phrases to be translated into a file CSV, PO or one file TGZ y exit___

___--i18n-import = (Filename.extension) Import one file CSV or PO with Translations and exit. The option '-l' is Necessary.___

___--i18n-overwrite Overwrites existing translation terms in the update of a module O import one file CSV o PO.___

___--modules = (Module a traslate) Specify modules to export. Use in combination with --i18n-exportation___