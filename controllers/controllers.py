# -*- coding: utf-8 -*-
from odoo import http

# class CashBox(http.Controller):
#     @http.route('/cash_box/cash_box/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cash_box/cash_box/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cash_box.listing', {
#             'root': '/cash_box/cash_box',
#             'objects': http.request.env['cash_box.cash_box'].search([]),
#         })

#     @http.route('/cash_box/cash_box/objects/<model("cash_box.cash_box"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cash_box.object', {
#             'object': obj
#         })