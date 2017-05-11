# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import time
import datetime
from odoo.exceptions import ValidationError


class outflow_seat(models.Model):
    _name = 'cash_box.outflow_seat'
    _rec_name = "employee"

    @api.model
    def _get_related_employee(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])

    @api.model
    def _get_euro(self):
        return self.env['res.currency.rate'].search([('rate', '=', 1)], limit=1).currency_id

    @api.model
    def _get_company_currency(self):
        # currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        currency_id = self.env['res.company']._company_default_get('cash_box').currency_id
        return currency_id or self._get_euro()

    @api.model
    def _get_datetime_now(self):
        return datetime.datetime.now()

    @api.model
    def print_report_details_movements(self):
        context = self.env.context
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'cash_box.report_details_movements_outflow',
            'context': context,
            'name': "details_movements_outflow_" + time.strftime('%Y_%m_%d')
        }

    @api.model
    def _get_total_amount_available(self):
        total_inflow = self._get_total_amount_inflow()
        total_outflow = self._get_total_amount_outflow()

        total_available = total_inflow - total_outflow
        return total_available

    @api.model
    def _get_total_amount_inflow(self):
        self.env.cr.execute("""SELECT COALESCE(SUM(amount),0) FROM cash_box_inflow_seat""")
        total_amount = self.env.cr.fetchone()

        return total_amount[0]

    @api.model
    def _get_total_amount_outflow(self):
        self.env.cr.execute("""SELECT COALESCE(SUM(amount),0) FROM cash_box_outflow_seat""")
        total_amount = self.env.cr.fetchone()

        return total_amount[0]

    @api.model
    def create(self, vals):
        total_available = self._get_total_amount_available()

        if total_available < vals.get("amount"):
            raise ValidationError(_('The amount entered exceeds the amount available'))

        if vals.get("amount") <= 0:
            raise ValidationError(_('The amount entered must be greater than zero'))

        return super(outflow_seat, self).create(vals)

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self._get_company_currency())
    employee = fields.Many2one('hr.employee', default=lambda self: self._get_related_employee(), string='Employee',
                               required=True,
                               readonly=True, help='')
    amount = fields.Monetary(string='Amount', help='Enter amount', required=True, currency_field='currency_id')
    description = fields.Text(string='Description', help='Enter a description', required=True)
    created_date = fields.Datetime(string='Created Date', required=True,
                                   default=lambda self: self._get_datetime_now())



class inflow_seat(models.Model):
    _name = 'cash_box.inflow_seat'
    _rec_name = "employee"

    @api.model
    def _get_related_employee(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])

    @api.model
    def _get_euro(self):
        return self.env['res.currency.rate'].search([('rate', '=', 1)], limit=1).currency_id

    @api.model
    def _get_company_currency(self):
        # currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        currency_id = self.env['res.company']._company_default_get('cash_box').currency_id
        return currency_id or self._get_euro()

    @api.model
    def _get_datetime_now(self):
        return datetime.datetime.now()

    @api.model
    def print_report_details_movements(self):
        context = self.env.context
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'cash_box.report_details_movements_inflow',
            'context': context,
            'name': "details_movements_inflow_" + time.strftime('%Y_%m_%d')
        }

    @api.model
    def create(self, vals):
        if vals.get("amount") <= 0:
            raise ValidationError(_('The amount entered must be greater than zero'))

        return super(inflow_seat, self).create(vals)

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self._get_company_currency())
    employee = fields.Many2one('hr.employee', default=lambda self: self._get_related_employee(), string='Employee',
                               required=True,
                               readonly=True, help='')
    amount = fields.Monetary(string='Amount', help='Enter amount', required=True, currency_field='currency_id')
    description = fields.Text(string='Description', help='Enter a description', required=True)
    created_date = fields.Datetime(string='Created Date', required=True,
                                   default=lambda self: self._get_datetime_now())
