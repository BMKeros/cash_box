# -*- coding: utf-8 -*-
{
    'name': "Cash Box",

    'summary': """
        Cash  Box is a module odoo 10 for management cash movement in a company""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dev Team BMKeros",
    'website': "http://dev.bmkeros.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/cash_box_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/inflow_seat_view.xml',
        'views/outflow_seat_view.xml',
        'reports/report_voucher_outflow.xml',
        'reports/report_voucher_inflow.xml'
    ],
    'qweb': [
        'static/src/xml/custom_button_print_movements_outflow_seat.xml',
        'static/src/xml/custom_button_print_movements_inflow_seat.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
