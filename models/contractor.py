# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contractor(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Contractor'
    _order = 'name'

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_budget_contractor = fields.Boolean(string="Is Contractor")
    alias = fields.Char(string="Alias")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_contact_ids = fields.One2many('res.partner',
                                  'contractor_contact_contractor_id',
                                  string="Contacts")
    # TODO: THIS IS TO BE REMOVE AND MOVE contract_ids to contractor_contract_ids
    contract_ids = fields.One2many('budget.contract',
                                  'contractor_id',
                                  string="Contracts")

    # Specified for which contractor it is, as contract_ids conflict to other inheritance such as section contract
    contractor_contract_ids = fields.One2many('budget.contract',
                                  'contractor_id',
                                  string="Contracts")

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('name_alias_uniq', 'unique(name, alias)', 'Name and Alias Must be Unique'),
    ]
