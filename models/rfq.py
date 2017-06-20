# -*- coding: utf-8 -*-
from lxml import etree
from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple, int_to_roman


class Rfq(models.Model):
    _name = 'budget.contractor.rfq'
    _rec_name = 'ref_no'
    _description = 'rfq'
    # _inherit = ['record.lock.mixin', 'mail.thread']

    # CHOICES
    # ----------------------------------------------------------
    # STATES = choices_tuple(['draft', 'rfq signed', 'on going', 'completed', 'cancelled', 'expired'],
    #                        is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    # state = fields.Selection(string='State', selection=STATES, default='draft', track_visibility='onchange')

    is_contract = fields.Boolean(string='For Contract', help='This RFQ is for a Contract')
    is_po = fields.Boolean(string='For Purchase Order', help='This RFQ is for a PO')
    is_digital = fields.Boolean(string='Is Digital')
    is_tool = fields.Boolean(string='Is Tool')

    ref_no = fields.Char(string='RFQ Reference')
    approval_no = fields.Char(string='Approval No')
    investment_area = fields.Char(string='Investment Area')
    owner = fields.Char(string='Owner')
    title = fields.Text(string='Title')
    justification = fields.Text(string='Justification')
    remark = fields.Text(string='Remark')

    amount = fields.Monetary(string='RFQ Amount', currency_field='company_currency_id')
    digital_investment_amount = fields.Monetary(string='Digital Investment Amount',
                                                currency_field='company_currency_id')

    approved_date = fields.Date(string='Sign Date')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    division_ids = fields.Many2many('budget.enduser.section', 'budget_division_rfq_rel',
                                    'contract_id', 'division_id',
                                    string="Divisions")
    # TODO TRASFERING SECTION TO DIVISION
    section_ids = fields.Many2many('budget.enduser.section',
                                   'budget_section_rfq_rel',
                                   'rfq_id', 'section_id',
                                   string="Sections")
    sub_section_ids = fields.Many2many('budget.enduser.sub.section',
                                       'budget_sub_section_rfq_rel',
                                       'rfq_id', 'sub_section_id',
                                       string="Sub Sections")

    contract_ids = fields.One2many('budget.contractor.contract',
                                    'rfq_id',
                                    string="Contracts")

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS FIELDS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('ref_no_uniq', 'unique(ref_no)', 'Already Exist')
    ]

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------

    # RECORD LOCK CONDITION
    # ----------------------------------------------------------
    # @api.one
    # @api.depends('state')
    # def _compute_is_record_lock(self):
    #     lock_states = ['draft', 'under verification', 'rfq signed']
    #     self.is_record_lock = True if self.state not in lock_states else False
