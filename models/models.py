# -*- coding: utf-8 -*-

from odoo import models, fields, api


class outflow_seat(models.Model):
    _name = 'cash_box.outflow_seat'

    user = fields.Char(help='Enter you user',required=True)
    amount = fields.Integer(help='Enter amount', required=True)
    description = fields.Text(help='Enter a description',required=True)
    date = fields.Datetime(help='Enter dates',required=True)


class inflow_seat(models.Model):
    _name = 'cash_box.inflow_seat'

    user = fields.Char(help='Enter you user', required=True)
    amount = fields.Integer(help='Enter amount', required=True)
    description = fields.Text(help='Enter a description', required=True)
    date = fields.Datetime(help='Enter dates', required=True)
