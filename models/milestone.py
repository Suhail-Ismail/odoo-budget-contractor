# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReadyForService(models.Model):
    _name = 'budget.contractor.milestone'
    _rec_name = 'reference_no'
    _description = 'Milestone'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    reference_no = fields.Char(string='Reference No')
    date = fields.Date(string='Date')

    # RELATIONSHIPS
    # ----------------------------------------------------------
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