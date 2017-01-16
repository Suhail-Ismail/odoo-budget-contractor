# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReadyForServiceActual(models.Model):
    _inherit = 'budget.contractor.rfs'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_actual = fields.Boolean(string='Is Actual')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractual_id = fields.Many2one('budget.contractor.rfs',
                                     string='Contractual',
                                     domain=[('is_actual','!=',True)])

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
