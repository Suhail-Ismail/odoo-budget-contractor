# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class VolumeDiscountRule(models.Model):
    _name = 'budget.contractor.discount.rule'
    _rec_name = 'name'
    _description = 'Volume Discount Rule'
    _order = 'id desc'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Char(default=lambda r: r._get_name())
    description = fields.Text()
    code = fields.Text()
    # RELATIONSHIPS
    # ----------------------------------------------------------
    contract_ids = fields.One2many('budget.contractor.contract',
                                   'discount_rule_id',
                                   string='Contract')

    # discount_ids = fields.One2many('budget.contractor.discount',
    #                                     'discount_rule_id',
    #                                     string='Discount')

    # DEFAULTS
    @api.model
    # ----------------------------------------------------------
    def _get_name(self):
        rule = self.search([], order='id desc', limit=1)
        if rule:
            sr = rule.id + 1
        else:
            sr = 1
        return 'Rule %03d' % sr


        # COMPUTE FIELDS
        # ----------------------------------------------------------

        # CONSTRAINS FIELDS
        # ----------------------------------------------------------

        # BUTTON ACTIONS / TRANSITIONS
        # ----------------------------------------------------------
