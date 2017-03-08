# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContractorContact(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Contractor Contact'

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_budget_contractor_contact = fields.Boolean(string="Is Contractor Contact")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_id = fields.Many2one('budget.contractor.contractor', string='New Contractor')

    # TODO DEPERCATED TO BE REMOVE
    contractor_contact_contractor_id = fields.Many2one('res.partner', string='Contractor')
