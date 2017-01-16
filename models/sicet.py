# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Sicet(models.Model):
    _name = 'budget.contractor.contract.sicet'
    _rec_name = 'name'
    _description = 'Sicet Type'

    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Char(string="Sicet Type")
    color = fields.Integer(string='Color Index')