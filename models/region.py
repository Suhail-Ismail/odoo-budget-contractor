# -*- coding: utf-8 -*-

from odoo import models, fields, api

# TODO: ADD THIS REGION TO INVOICE
class Region(models.Model):
    _name = 'budget.region'
    _rec_name = 'alias'
    _description = 'Region'

    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Char(string='Region Name')
    alias = fields.Char(string='Alias Name')
