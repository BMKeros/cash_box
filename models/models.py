# -*- coding: utf-8 -*-

from odoo import models, fields, api

class outflow_seat(models.Model):
	# nombre del modele - nombre de la clase
    _name = 'cash_box.outflow_seat'

    user = fields.Char()
    amount = fields.Integer()
    description = fields.Char()
    date = fields.Datetime()
    # fecha_registro = fields.Date(auto_now_add=True, auto_now=False)

class inflow_seat(models.Model):
    
    _name = 'cash_box.inflow_seat'

    user= fields.Char()
    amount= fields.Integer()
    description= fields.Char()
    date= fields.Datetime()