# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BudgetInherit(models.Model):
    _inherit = 'budget.core.budget'

    total_contracted_amount = fields.Monetary(compute="_compute_total_contracted_amount",
                                              currency_field='company_currency_id',
                                              string='Total Contracted Amount',
                                              default=0.00)
    # RELATIONSHIPS
    # ----------------------------------------------------------
    # company_currency_id exist in budget.core.budget already
    contract_ids = fields.One2many('budget.contractor.contract',
                                   'budget_id',
                                   string="Contracts")

    @api.one
    @api.depends('contract_ids', 'contract_ids.amount')
    def _compute_total_contracted_amount(self):
        self.total_contracted_amount = sum(self.contract_ids.mapped('amount'))