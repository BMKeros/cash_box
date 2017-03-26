# -*- coding: utf-8 -*-

from odoo import models, fields, api


class outflow_seat(models.Model):
    _name = 'cash_box.outflow_seat'

    employee = fields.Many2one('res.users',default=lambda self: self.env.user, string='Employee', required=True, readonly=True, help='');
    amount = fields.Float(string='Amount',help='Enter amount', required=True)
    description = fields.Text(string='Description',help='Enter a description',required=True)


class inflow_seat(models.Model):
    _name = 'cash_box.inflow_seat'

    employee = fields.Many2one('res.users',default=lambda self: self.env.user, string='Employee', required=True, readonly=True, help='');
    amount = fields.Float(string='Amount', help='Enter amount', required=True)
    description = fields.Text(string='Description', help='Enter a description', required=True)
