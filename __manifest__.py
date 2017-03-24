# -*- coding: utf-8 -*-
{
    'name': "Cash Box",

    'summary': """
        Cash  Box is a module odoo 10 for management move cash in a company""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Team Dev BMKeros",
    'website': "http://dev.bmkeros.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inflow_seat_view.xml',
        'views/outflow_seat_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}