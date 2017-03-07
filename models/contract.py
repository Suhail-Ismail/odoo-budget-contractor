# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Contract(models.Model):
    _name = 'budget.contractor.contract'
    _rec_name = 'contract_ref'
    _description = 'Contract'

    # CHOICES
    # ----------------------------------------------------------
    # TODO DEPRECATED
    BUDGET_TYPES = choices_tuple(['capex', 'opex'])
    CATEGORIES = choices_tuple(['consultancy', 'license', 'service', 'supply', 'support', 'turnkey'])
    STATES = choices_tuple(['draft', 'yet to commission', 'on going', 'cancelled', 'expired'], is_sorted=False)
    CHANGE_TYPES = choices_tuple(['principal', 'amendment', 'addendum'], is_sorted=False)
    VERSIONS = [(i, '%d - %s' % (i, int_to_roman(i))) for i in range(1, 100)]
    CONTRACT_TYPES = choices_tuple(['rate', 'rfq', 'priced', 'support','consultancy',
                                    'license', 'service', 'supply', 'turnkey'], is_sorted=False)
    DELIVERY_TERMS = choices_tuple(['fob', 'cip', 'cif', 'ddp', 'monthly'], is_sorted=False)
    OPEX_SERVICES = choices_tuple(['maintenance', 'repair and service'], is_sorted=False)
    VENDOR_BASES = choices_tuple(['local', 'overseas'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='draft', track_visibility='onchange')

    is_opex = fields.Boolean(string='Is Opex')
    is_capex = fields.Boolean(string='Is Capex')

    # TODO DEPRECATED
    is_contract = fields.Boolean(string='Is Contract')
    # TODO DEPRECATED
    is_rfq = fields.Boolean(string='Is RFQ')

    no = fields.Char(string="No")
    # TODO DEPRECATED
    budget_type = fields.Selection(string='Budget Type', selection=BUDGET_TYPES)
    change_type = fields.Selection(string='Change Type', selection=CHANGE_TYPES, default='principal')
    version = fields.Selection(string='Version', selection=VERSIONS)
    contract_type = fields.Selection(string='Contract Type', selection=CONTRACT_TYPES)
    delivery_term = fields.Selection(string='Delivery Term', selection=DELIVERY_TERMS)
    opex_service = fields.Selection(string='OPEX Service', selection=OPEX_SERVICES)
    vendor_base = fields.Selection(string='OPEX Service', selection=VENDOR_BASES, default='local')

    # TODO DEPRECATED
    category = fields.Selection(string='Category', selection=CATEGORIES)

    # TODO DEPRECATED
    remarks = fields.Text(string='Remarks')

    owner = fields.Char(string='Owner')
    volume_discount_ref = fields.Char(string='Volume Discount Reference')

    remark = fields.Text(string='Remarks')
    description = fields.Text(string='Description')
    year_count = fields.Integer(string='# of Years')
    foc_service_month_count = fields.Integer(string='FOC Service # of Months')
    extended_warranty_count = fields.Integer(string='Extended Warranty # of Months')

    amount = fields.Monetary(string='Contract Amount', currency_field='company_currency_id')
    cost_per_month = fields.Monetary(string='Cost per Month', currency_field='company_currency_id')
    cost_per_year = fields.Monetary(string='Cost per Year', currency_field='company_currency_id')
    hardware_amount = fields.Monetary(string='Hardware Amount', currency_field='company_currency_id')
    software_amount = fields.Monetary(string='Software Amount', currency_field='company_currency_id')
    service_amount = fields.Monetary(string='Service Amount', currency_field='company_currency_id')
    future_voucher_amount = fields.Monetary(string='Future Voucher Amount', currency_field='company_currency_id')
    voucher_utilized_amount = fields.Monetary(string='Voucher Utilized Amount', currency_field='company_currency_id')
    foc_service_amount = fields.Monetary(string='FOC Service Amount', currency_field='company_currency_id')
    extended_warranty_amount = fields.Monetary(string='Extended Warranty Amount', currency_field='company_currency_id')

    support_percentage = fields.Float(string='Support Percentage', digits=(5, 2))
    maintenance_percentage = fields.Float(string='Maintenance Percentage', digits=(5, 2))
    spare_percentage = fields.Float(string='Spare Percentage', digits=(5, 2))

    # TODO DEPRECATED
    material_amount = fields.Monetary(string='Material Amount', currency_field='company_currency_id')

    sign_date = fields.Date(string='Sign Date')
    commencement_date = fields.Date(string='Commencement Date')
    end_date = fields.Date(string='End Date')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contractor_id = fields.Many2one('res.partner', string='Contractor', domain=[('is_budget_contractor', '=', True)])

    voucher_utilized_from_contract_id = fields.Many2one('budget.contractor.contract', string='Contract')

    # capex_budget_ids = fields.Many2many('budget.core.budget',
    #                                     'capex_budget_contract_rel',
    #                                     'contract_id',
    #                                     'capex_budget_id',
    #                                     string='Capex Budget',
    #                                     domain=[('is_project', '=', True)])

    # opex_budget_ids = fields.Many2many('budget.core.budget',
    #                                    'opex_budget_contract_rel',
    #                                    'contract_id',
    #                                    'capex_budget_id',
    #                                    string='Capex Budget',
    #                                    domain=[('is_operation', '=', True)])

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
    sub_section_ids = fields.Many2many('res.partner',
                                       'sub_section_contract_rel',
                                       'contract_id',
                                       'sub_section_id',
                                       string="Sub Sections",
                                       domain="[('is_budget_sub_section','=',True)]"
                                       )

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    year = fields.Char(string="Year",
                       compute='_compute_year',
                       inverse='_set_year',
                       store=True)
    contract_ref = fields.Char(string="Contract Reference",
                               compute='_compute_contract_ref',
                               store=True)

    @api.one
    @api.depends('no', 'change_type', 'version', 'contractor_id.alias')
    def _compute_contract_ref(self):
        change_type = '' if self.change_type == 'principal' else self.change_type
        contract_ref = "{}/{} {} {}".format(self.no or '',
                                            self.contractor_id.alias or '',
                                            change_type,
                                            self.version or '').upper()
        self.contract_ref = contract_ref.strip()

    @api.one
    @api.depends('no')
    def _compute_year(self):
        pass

    @api.one
    def _set_year(self):
        pass

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
