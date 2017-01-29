# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Contract(models.Model):
    _name = 'budget.contractor.contract'
    _rec_name = 'contract_ref'
    _description = 'Contract'

    # CHOICES
    # ----------------------------------------------------------
    BUDGET_TYPES = choices_tuple(['capex', 'opex'])
    CATEGORIES = choices_tuple(['consultancy', 'license', 'service', 'supply', 'support', 'turnkey'])
    STATES = choices_tuple(['active', 'closed'], is_sorted=False)
    CHANGE_TYPES = choices_tuple(['principal', 'amendment', 'addendum'], is_sorted=False)
    VERSIONS = [(i, '%d - %s' % (i, int_to_roman(i))) for i in range(1, 100)]
    SICET_TYPES = choices_tuple(['2a', '2b', '3'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='active')

    is_contract = fields.Boolean(string='Is Contract')

    contract_no = fields.Char(string="Contract No")
    budget_type = fields.Selection(string='Budget Type', selection=BUDGET_TYPES)
    change_type = fields.Selection(string='Change Type', selection=CHANGE_TYPES, default='principal')
    version = fields.Selection(string='Version', selection=VERSIONS)

    amount = fields.Monetary(string='Contract Amount', currency_field='company_currency_id')
    service_amount = fields.Monetary(string='Service Amount', currency_field='company_currency_id')
    material_amount = fields.Monetary(string='Material Amount', currency_field='company_currency_id')

    category = fields.Selection(string='Category', selection=CATEGORIES)

    sign_date = fields.Date(string='Sign Date')
    commencement_date = fields.Date(string='Commencement Date')
    end_date = fields.Date(string='End Date')
    remarks = fields.Text(string='Remarks')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contractor_id = fields.Many2one('res.partner', string='Contractor', domain=[('is_budget_contractor', '=', True)])
    rfs_ids = fields.One2many('budget.contractor.rfs',
                              'contract_id',
                              string="Ready for Service Certificates")
    milestone_ids = fields.One2many('budget.contractor.milestone',
                                    'contract_id',
                                    string="Milestones")
    sicet_type_ids = fields.Many2many('budget.contractor.contract.sicet',
                                      'sicet_contract_rel',
                                      'contract_id',
                                      'sicet_id',
                                      string='Sicet Type')
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
        change_type = '' if self.change_type == 'principal' else self.change_type
        contract_ref = "{}/{} {} {}".format(self.contract_no or '',
                                                 self.contractor_id.alias or '',
                                                 change_type,
                                                 self.version or '').upper()
        self.contract_ref = contract_ref.strip()
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
