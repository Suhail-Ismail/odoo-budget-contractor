# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_core.models.utilities import choices_tuple, int_to_roman

class Contract(models.Model):
    _name = 'budget.contractor.contract'
    _rec_name = 'contract_ref'
    _description = 'Contract'

    # CHOICES
    # ----------------------------------------------------------
    CATEGORIES = choices_tuple(['consultancy', 'license', 'service', 'supply', 'support', 'turnkey'])
    STATES = choices_tuple(['active', 'closed'], is_sorted=False)
    CHANGE_TYPES = choices_tuple(['principal', 'amendment', 'addendum'], is_sorted=False)
    VERSIONS = [(i, '%d - %s' % (i, int_to_roman(i))) for i in range(1, 100)]
    SICET_TYPES = choices_tuple(['2a', 'a2/2b', '2b', '3'], is_sorted=False)
    SUB_SICET_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)
    SYSTEM_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)
    NETWORK_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='active')

    contract_no = fields.Char(string="Contract No")
    sicet_type = fields.Selection(SICET_TYPES)
    change_type = fields.Selection(CHANGE_TYPES, default='principal')
    version = fields.Selection(VERSIONS)

    amount = fields.Monetary(string='Contract Amount', currency_field='company_currency_id')
    service_amount = fields.Monetary(string='Service Amount', currency_field='company_currency_id')
    material_amount = fields.Monetary(string='Material Amount', currency_field='company_currency_id')

    category = fields.Selection(CATEGORIES)
    # sub_sicet_type = fields.Selection(SUB_SICET_TYPES)
    # system_type = fields.Selection(SYSTEM_TYPES)
    # network_type = fields.Selection(NETWORK_TYPES)

    sign_date = fields.Date(string='Sign Date')
    commencement_date = fields.Date(string='Commencement Date')
    end_date = fields.Date(string='End Date')
    remarks = fields.Text(string='Remarks')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    budget_id = fields.Many2one('budget.core.budget', string='Budget No')
    contractor_id = fields.Many2one('res.partner', string='Contractor', domain=[('is_budget_contractor','=', True)])
    section_ids = fields.Many2many('res.partner',
                                'section_contract_rel',
                                'contract_id',
                                'section_id',
                                string="Sections",
                                domain="[('is_budget_section','=',True)]"
                                )

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    contract_ref = fields.Char(string="Contract Reference",
                               compute='_compute_contract_ref',
                               store=True)

    @api.one
    @api.depends('contract_no', 'change_type', 'version', 'contractor_id.alias')
    def _compute_contract_ref(self):
        change_type = '' if self.change_type == 'principal' and not self.change_type else self.change_type
        self.contract_ref = "{}/{} {} {}".format(self.contract_no or '',
                                                 self.contractor_id.alias or '',
                                                 change_type,
                                                 self.version or '').upper()

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('contract_ref_uniq', 'unique(contract_ref)', 'Already Exist'),
    ]

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2close(self):
        self.state = 'closed'
