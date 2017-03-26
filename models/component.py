# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple

class Component(models.Model):
    _name = 'budget.contractor.component'
    _rec_name = 'name'
    _description = 'Contract Component'
    _order = 'sequence'

    # CHOICES
    # ----------------------------------------------------------
    NAMES = choices_tuple(['equipment', 'software', 'installation services',
                           'consultancy', 'support and maintenance',
                           'team based hiring', 'spare', 'return and repair',
                           'managed service'], is_sorted=False)
    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Selection(string='Name', selection=NAMES)

    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence')
    unit = fields.Integer(string='Unit')
    amount = fields.Monetary(string='Amount', currency_field='company_currency_id')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
