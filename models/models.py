# -*- coding: utf-8 -*-
from odoo import models, fields, api


class outflow_seat(models.Model):
    _name = 'cash_box.outflow_seat'
    _rec_name = "employee"

    @api.model
    def _get_euro(self):
        return self.env['res.currency.rate'].search([('rate', '=', 1)], limit=1).currency_id

    @api.model
    def _get_company_currency(self):
        # currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        currency_id = self.env['res.company']._company_default_get('cash_box').currency_id
        return currency_id or self._get_euro()

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self._get_company_currency())
    employee = fields.Many2one('res.users', default=lambda self: self.env.user, string='Employee', required=True,
                               readonly=True, help='')
    amount = fields.Monetary(string='Amount', help='Enter amount', required=True, currency_field='currency_id')
    description = fields.Text(string='Description', help='Enter a description', required=True)


class inflow_seat(models.Model):
    _name = 'cash_box.inflow_seat'
    _rec_name = "employee"

    @api.model
    def _get_euro(self):
        return self.env['res.currency.rate'].search([('rate', '=', 1)], limit=1).currency_id

    @api.model
    def _get_company_currency(self):
        # currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        currency_id = self.env['res.company']._company_default_get('cash_box').currency_id
        return currency_id or self._get_euro()

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self._get_company_currency())
    employee = fields.Many2one('res.users', default=lambda self: self.env.user, string='Employee', required=True,
                               readonly=True, help='')
    amount = fields.Monetary(string='Amount', help='Enter amount', required=True, currency_field='currency_id')
    description = fields.Text(string='Description', help='Enter a description', required=True)
