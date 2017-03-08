# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

from odoo.exceptions import ValidationError

# TODO TO BE REMOVE AFTER EVERYTHING REFERRING TO THIS IS CLEARED
class Contractor(models.Model):
    _inherit = 'res.partner'

    # BASIC FIELDS
    # alias exist already
    # ----------------------------------------------------------
    is_budget_contractor = fields.Boolean(string="Is Contractor")


    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_contact_ids = fields.One2many('res.partner',
                                  'contractor_contact_contractor_id',
                                  string="Contractor Contacts")
    contractor_contract_ids = fields.One2many('budget.contractor.contract',
                                  'contractor_id',
                                  string="Contractor Contracts")
    partner_id = fields.Many2one('res.partner', string='Contractor')
    contact_ids = fields.One2many('res.partner',
                                  'contractor_contact_contractor_id',
                                  string="Contractor Contacts")
    # CONSTRAINS
    # ----------------------------------------------------------
    contract_count = fields.Integer(compute='_compute_contract_count', string="Contract Count")

    @api.one
    @api.depends('contractor_contract_ids')
    def _compute_contract_count(self):
        self.contract_count = len(self.contractor_contract_ids)

    # CONSTRAINS
    # ----------------------------------------------------------
    @api.one
    @api.constrains('alias')
    def _check_alias(self):
        if re.search('\s', unicode(self.alias)):
            raise ValidationError('spaces are not allowed in ALIAS')

    _sql_constraints = [
        ('alias_uniq', 'unique(alias)', 'Alias Must be Unique'),
    ]

    # MISC METHODS
    # ----------------------------------------------------------
    @api.onchange('alias')
    def _upper_alias(self):
        if self.alias:
            self.alias = self.alias.upper()