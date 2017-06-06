# -*- coding: utf-8 -*-
from odoo import http

# class BudgetContractor(http.Controller):
#     @http.route('/budget_contractor/budget_contractor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/budget_contractor/budget_contractor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('budget_contractor.listing', {
#             'root': '/budget_contractor/budget_contractor',
#             'objects': http.request.env['budget_contractor.budget_contractor'].search([]),
#         })

#     @http.route('/budget_contractor/budget_contractor/objects/<model("budget_contractor.budget_contractor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('budget_contractor.object', {
#             'object': obj
#         })