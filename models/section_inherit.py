# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Section(models.Model):
    _inherit = 'res.partner'

    # RELATIONSHIPS
    # ----------------------------------------------------------
    section_contract_ids = fields.Many2many('budget.contract',
                                            'section_contract_rel',
                                            'section_id', 'contract_id', string="Contracts")
