# -*- coding: utf-8 -*-
from lxml import etree
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Contract(models.Model):
    _name = 'budget.contractor.contract.system.type'
    _rec_name = 'name'
    _description = 'Contract System Type'

    # BASIC FIELDS
    # ----------------------------------------------------------
    active = fields.Boolean(default=True)

    name = fields.Char(string="Name")

    # CONSTRAINS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Already Exist'),
    ]
