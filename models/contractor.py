# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple
import re

from odoo.exceptions import ValidationError


class Contractor(models.Model):
    _name = 'budget.contractor.contractor'
    _description = 'Contractor'
    _rec_name = 'name'
    _inherit = ['budget.res.partner.mixin']

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------


    # RELATIONSHIPS
    # ----------------------------------------------------------
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
