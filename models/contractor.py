# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

from odoo.exceptions import ValidationError


class Contractor(models.Model):
    _inherit = 'res.partner'

    # BASIC FIELDS
    # ----------------------------------------------------------
    is_budget_contractor = fields.Boolean(string="Is Contractor")
    alias = fields.Char(string="Alias")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_contact_ids = fields.One2many('res.partner',
                                  'contractor_contact_contractor_id',
                                  string="Contractor Contacts")
    # TODO CHECK THE POSSIBILITY OF USING THE DEFAULT CONTACT XML AND CONTACTS
    contractor_contract_ids = fields.One2many('budget.contractor.contract',
                                  'contractor_id',
                                  string="Contractor Contracts")

    # CONSTRAINS
    # ----------------------------------------------------------
    total_contract = fields.Integer(compute='_compute_total_contract', string="Total Contracts")

    @api.one
    @api.depends('contractor_contract_ids')
    def _compute_total_contract(self):
        self.total_contract = len(self.contractor_contract_ids)

    # CONSTRAINS
    # ----------------------------------------------------------
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