# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple
import re

from odoo.exceptions import ValidationError


class Contractor(models.Model):
    _name = 'budget.contractor.contractor'
    _description = 'Contractor'
    _rec_name = 'name'
    _inherit = ['partner.mixin']

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'inactive'])

    # BASIC FIELDS
    # name exist already
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='active')

    alias = fields.Char(string="Alias")

    remark = fields.Text(string='Remarks')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    # TODO CONSIDER MAKING A SEPERATE OBJECT NOT RES.PARTNER
    contact_ids = fields.One2many('res.partner',
                                  'contractor_id',
                                  string="Contractor Contacts")

    contract_ids = fields.One2many('budget.contractor.contract',
                                   'contractor_id',
                                   string="Contractor Contracts")

    # CONSTRAINS
    # ----------------------------------------------------------
    contract_count = fields.Integer(compute='_compute_contract_count', string="Contract Count")

    @api.one
    @api.depends('contract_ids')
    def _compute_contract_count(self):
        self.contract_count = len(self.contract_ids)

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
