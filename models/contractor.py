# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Contractor(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Contractor'

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_budget_contractor = fields.Boolean(string="Is Contractor")
    alias = fields.Char(string="Alias")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contact_ids = fields.One2many('res.partner',
                                  'contractor_id',
                                  string="Contacts")

    contract_ids = fields.One2many('budget.contract',
                                  'contractor_id',
                                  string="Contracts")