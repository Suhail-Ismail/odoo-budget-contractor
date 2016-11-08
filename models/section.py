# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Section(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Section'

    # BASIC FIELDS
    # name exist already
    # alias exist already
    # ----------------------------------------------------------
    is_budget_section = fields.Boolean(string='Is Budget Section')

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    # Specified for which section it is, as contract_ids conflict to other inheritance such as contractor contract
    section_contract_ids = fields.One2many('budget.contract',
                                  'section_id',
                                  string="Contracts")

# TODO: SUB SECTION NOT YET PROPERLY IMPLEMENTED
class SubSection(models.Model):
    _name = 'budget.section.sub'
    _rec_name = 'alias'
    _description = 'Sub Section'

    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Char(string='Sub Section Name')
    alias = fields.Char(string='Alias Name')
