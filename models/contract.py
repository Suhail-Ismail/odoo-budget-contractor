# -*- coding: utf-8 -*-
from lxml import etree
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Contract(models.Model):
    _name = 'budget.contractor.contract'
    _rec_name = 'contract_ref'
    _description = 'Contract'
    _inherit = ['record.lock.mixin', 'mail.thread']

    # TODO: TO BE REMOVE WHEN FINALIZED / DEPRECATED
    # ----------------------------------------------------------
    BUDGET_TYPES = choices_tuple(['capex', 'opex'])
    OPEX_SERVICES = choices_tuple(['maintenance', 'spare', 'repair and return', 'support', 'managed service'])
    CATEGORIES = choices_tuple(['consultancy', 'license', 'service', 'supply', 'support', 'turnkey'])
    SYSTEM_TYPES = choices_tuple(['cloud', 'dwdm', 'gpon', 'load balancer', 'ngn', 'nms',
                                  'noc', 'proxy cache', 'servers', 'softswitch', 'watchguard',
                                  'web filtering'], is_sorted=False)

    cost_per_month = fields.Monetary(string='Cost per Month', currency_field='company_currency_id')
    cost_per_year = fields.Monetary(string='Cost per Year', currency_field='company_currency_id')
    budget_type = fields.Selection(string='Budget Type', selection=BUDGET_TYPES)
    is_contract = fields.Boolean(string='Is Contract')
    is_rfq = fields.Boolean(string='Is RFQ')
    opex_service = fields.Selection(string='OPEX Service', selection=OPEX_SERVICES)
    category = fields.Selection(string='Category', selection=CATEGORIES)
    remarks = fields.Text(string='Remarks')
    material_amount = fields.Monetary(string='Material Amount', currency_field='company_currency_id')
    end_date = fields.Date(string='End Date')
    year_count = fields.Integer(string='# of Years')
    support_percentage = fields.Float(string='Support Percentage', digits=(5, 2))
    maintenance_percentage = fields.Float(string='Maintenance Percentage', digits=(5, 2))
    spare_percentage = fields.Float(string='Spare Percentage', digits=(5, 2))
    volume_discount_ref = fields.Char(string='Volume Discount Reference')
    system_type = fields.Selection(string='System Type', selection=SYSTEM_TYPES)

    old_contractor_id = fields.Many2one('res.partner', string='Old Contractor',
                                        domain=[('is_budget_contractor', '=', True)])
    old_section_ids = fields.Many2many('res.partner', 'section_contract_rel', 'contract_id', 'section_id',
                                       string="Old Sections", domain=[('is_budget_section', '=', True)])
    old_sub_section_ids = fields.Many2many('res.partner', 'sub_section_contract_rel', 'contract_id', 'sub_section_id',
                                           string="Old Sub Sections", domain=[('is_budget_sub_section', '=', True)])
    sicet_type_ids = fields.Many2many('budget.contractor.contract.sicet', 'sicet_contract_rel', 'contract_id',
                                      'sicet_id', string='Sicet Type')

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['draft', 'contract signed', 'on going', 'completed', 'cancelled', 'expired'],
                           is_sorted=False)
    CHANGE_TYPES = choices_tuple(['principal', 'amendment', 'addendum'], is_sorted=False)
    VERSIONS = [(i, '%d - %s' % (i, int_to_roman(i))) for i in range(1, 100)]
    CONTRACT_TYPES = choices_tuple(['rfq', 'sicet 2a', 'sicet 2b', 'sicet 3'], is_sorted=False)
    CONTRACT_SCOPES = choices_tuple(
        ['supply and installation', 'procurement', 'consultancy', 'support license', 'service', 'others'],
        is_sorted=False)
    PAYMENT_TYPES = choices_tuple(['rate', 'fixed price', 'others'],
                                  is_sorted=False)
    DELIVERY_TERMS = choices_tuple(['fob', 'cip', 'cif', 'ddp', 'monthly', 'others'], is_sorted=False)
    VENDOR_BASES = choices_tuple(['local', 'overseas'], is_sorted=False)
    NETWORK_TYPES = choices_tuple(['fixed', 'mobile', 'transmission'], is_sorted=False)
    NETWORK_LAYERS = choices_tuple(['last mile', 'access', 'aggregation', 'core', 'transmission',
                                    'service delivery', 'power', 'nms', 'digital', 'cpe and others'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='draft', track_visibility='onchange')
    network_type = fields.Selection(string='Network Type', selection=NETWORK_TYPES)
    network_layer = fields.Selection(string='Network Layer', selection=NETWORK_LAYERS)

    is_opex = fields.Boolean(string='Is Opex')
    is_capex = fields.Boolean(string='Is Capex')

    no = fields.Char(string="Contract No")
    change_type = fields.Selection(string='Change Type', selection=CHANGE_TYPES, default='principal')
    version = fields.Selection(string='Version', selection=VERSIONS)
    contract_type = fields.Selection(string='Contract Type', selection=CONTRACT_TYPES)
    # TODO CONFIRM TO AZAR/RISHAD IF IT SHOULD BE REMOVE
    contract_scope = fields.Selection(string='Contract Scope', selection=CONTRACT_SCOPES)
    payment_type = fields.Selection(string='Payment Type', selection=PAYMENT_TYPES)
    delivery_term = fields.Selection(string='Delivery Term', selection=DELIVERY_TERMS)
    vendor_base = fields.Selection(string='OPEX Service', selection=VENDOR_BASES, default='local')
    url = fields.Char(string='Contract URL')
    year = fields.Char(string="Year")

    owner = fields.Char(string='Owner')

    remark = fields.Text(string='Remarks')
    description = fields.Text(string='Description')
    month_count = fields.Integer(string='# of Months')
    foc_service_month_count = fields.Integer(string='FOC Service # of Months')
    extended_warranty_count = fields.Integer(string='Extended Warranty # of Months')
    normal_warranty_count = fields.Integer(string='Normal Warranty # of Months')

    amount = fields.Monetary(string='Contract Amount', currency_field='company_currency_id')
    discount_amount = fields.Monetary(string='Discount Amount', currency_field='company_currency_id')
    hardware_amount = fields.Monetary(string='Hardware Amount', currency_field='company_currency_id')
    software_amount = fields.Monetary(string='Software Amount', currency_field='company_currency_id')
    service_amount = fields.Monetary(string='Service Amount', currency_field='company_currency_id')
    future_voucher_amount = fields.Monetary(string='Future Voucher Amount', currency_field='company_currency_id')
    voucher_utilized_amount = fields.Monetary(string='Voucher Utilized Amount', currency_field='company_currency_id')
    training_amount = fields.Monetary(string='Training Amount', currency_field='company_currency_id')

    sign_date = fields.Date(string='Sign Date')
    commencement_date = fields.Date(string='Commencement Date')
    expiry_date = fields.Date(string='Expiry Date')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    system_type_id = fields.Many2one('budget.contractor.contract.system.type', string='System Type')
    contractor_id = fields.Many2one('budget.contractor.contractor', string='Contractor')
    rfq_id = fields.Many2one('budget.contractor.rfq', string='RFQ',
                             domain="[('contract_ids','=',False)]")
    section_ids = fields.Many2many('budget.enduser.section', 'budget_section_contract_rel',
                                   'contract_id', 'section_id',
                                   string="Sections", )
    sub_section_ids = fields.Many2many('budget.enduser.sub.section',
                                       'budget_sub_section_contract_rel',
                                       'contract_id', 'sub_section_id',
                                       string="Sub Sections")
    voucher_utilized_from_contract_id = fields.Many2one('budget.contractor.contract', string='Contract')
    rfs_ids = fields.One2many('budget.contractor.rfs',
                              'contract_id',
                              string="Ready for Service Certificates")
    milestone_ids = fields.One2many('budget.contractor.milestone',
                                    'contract_id',
                                    string="Milestones")
    component_ids = fields.One2many('budget.contractor.component',
                                    'contract_id',
                                    string="Components")

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    contract_ref = fields.Char(string="Contract Reference",
                               compute='_compute_contract_ref',
                               store=True)

    @api.one
    @api.depends('no', 'year', 'change_type', 'version', 'contractor_id.alias')
    def _compute_contract_ref(self):
        change_type = False if self.change_type == 'principal' else self.change_type
        # PATTERN NO/ALIAS ADD VI
        string_list = [i for i in [self.no, self.year, self.contractor_id.alias] if i is not False]
        contract_ref = '/'.join(string_list)

        roman = '' if not self.version else int_to_roman(self.version)
        string_list = [i for i in [contract_ref, change_type, roman] if i is not False]
        contract_ref = ' '.join(string_list).upper()

        self.contract_ref = contract_ref.strip()

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('contract_ref_uniq', 'unique(contract_ref)', 'Already Exist'),
        ('contract_capex_or_opex_required', 'CHECK(is_opex OR is_capex)', 'MUST SELECT EITHER CAPEX OR OPEX OR BOTH'),
    ]

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2contract_signed(self):
        self.state = 'contract signed'

    @api.one
    def set2on_going(self):
        self.state = 'on going'

    @api.one
    def set2close(self):
        self.state = 'closed'

    # RECORD LOCK CONDITION
    # ----------------------------------------------------------
    @api.one
    @api.depends('state')
    def _compute_is_record_lock(self):
        lock_states = ['draft', 'under verification', 'contract signed']
        self.is_record_lock = True if self.state not in lock_states else False
