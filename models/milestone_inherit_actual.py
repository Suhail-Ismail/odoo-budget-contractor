# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MilestoneActual(models.Model):
    _inherit = 'budget.contractor.milestone'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_actual = fields.Boolean(string='Is Actual')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractual_id = fields.Many2one('budget.contractor.milestone',
                                     string='Contractual',
                                     domain=[('is_actual','!=',True)])

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
