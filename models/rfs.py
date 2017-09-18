# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ReadyForService(models.Model):
    _name = 'budget.contractor.rfs'
    _rec_name = 'reference_no'
    _description = 'Ready For Service'

    # TODO DEPRECATED
    reference_no = fields.Char(string='Reference No')
    actual_ids = fields.One2many('budget.contractor.rfs',
                                 'contractual_id',
                                 string="Actuals",
                                 domain=[('is_actual','=',True)])

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    sequence = fields.Integer(string='Sequence')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contract_id = fields.Many2one('budget.contractor.contract', string='Contract')

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
