# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ContractorContact(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Contractor Contact'

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_budget_contractor_contact = fields.Boolean(string="Is Contractor")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_id = fields.Many2one('res.partner', string='Contractor')
