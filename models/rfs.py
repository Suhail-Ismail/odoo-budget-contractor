# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ReadyForService(models.Model):
    _name = 'budget.contractor.rfs'
    _rec_name = 'reference_no'
    _description = 'Ready For Service'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    reference_no = fields.Char(string='Reference No')
    date = fields.Date(string='Date')
    amount = fields.Monetary(string='Amount', currency_field='company_currency_id')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')
    actual_ids = fields.One2many('budget.contractor.rfs',
                                 'contractual_id',
                                 string="Actuals",
                                 domain=[('is_actual','=',True)])

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
