# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

from odoo.exceptions import ValidationError


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

    # CONSTRAINS
    # ----------------------------------------------------------
    # TODO: NEED TO CHECK INDIVIDUAL UNIQUENESS FOR NAME AND ALIAS
    # TODO: DISALLOW SPACE IN ALIAS
    @api.one
    @api.constrains('alias')
    def _check_alias(self):
        if re.search('\s', unicode(self.alias)):
            raise ValidationError('spaces are not allowed in ALIAS')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name Must be Unique'),
        ('alias_uniq', 'unique(alias)', 'Alias Must be Unique'),
    ]

    # MISC METHODS
    # ----------------------------------------------------------
    @api.onchange('alias')
    def _upper_alias(self):
        if self.alias:
            self.alias = self.alias.upper()