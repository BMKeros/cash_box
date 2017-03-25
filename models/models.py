# -*- coding: utf-8 -*-

from odoo import models, fields, api


class outflow_seat(models.Model):
    _name = 'cash_box.outflow_seat'

    employee = fields.Char(srting='Employee',help='Enter you user',required=True)
    amount = fields.Integer(string='Amount',help='Enter amount', required=True)
    description = fields.Text(string='Description',help='Enter a description',required=True)
    date = fields.Datetime(string='Date',help='Enter date',required=True)


class inflow_seat(models.Model):
    _name = 'cash_box.inflow_seat'

    employee = fields.Char(srting='Employee', help='Enter you user', required=True)
    amount = fields.Integer(string='Amount', help='Enter amount', required=True)
    description = fields.Text(string='Description', help='Enter a description', required=True)
    date = fields.Datetime(string='Date', help='Enter date', required=True)
