# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple

class Milestone(models.Model):
    _name = 'budget.contractor.milestone'
    _rec_name = 'name'
    _description = 'Milestone'
    _order = 'sequence'

    # CHOICES
    # ----------------------------------------------------------
    NAMES = choices_tuple(['delivery sicet-2a', 'ready for service (rfs)', 'provisional acceptance certificate (pac)',
                           'service sicet-2a', 'delivery sicet-2b', 'service sicet-2b', 'progressive payment',
                           'completion certificate', 'retention at completion certificate', 'retention at end of Maintenance',
                           'team based hiring', 'consultancy', 'support and maintenance', 'others'], is_sorted=False)
    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Selection(string='Name', selection=NAMES)
    sequence = fields.Integer(string='Sequence')
    date = fields.Date(string='Date')
    amount = fields.Monetary(string='Amount', currency_field='company_currency_id')

    # TODO DEPRECATED or use as reference "CONTRACT AND MILESTONE"
    reference_no = fields.Char(string='Reference No')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')
    actual_ids = fields.One2many('budget.contractor.milestone',
                                 'contractual_id',
                                 string="Actuals",
                                 domain=[('is_actual','=',True)])

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
