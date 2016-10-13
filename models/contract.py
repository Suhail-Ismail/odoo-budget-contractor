# -*- coding: utf-8 -*-
from openerp import models, fields, api
from .utils import choices_tuple

# MISC FUNCTIONS
# --------------------------------------------------------------------------------------------------

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, int):
        raise TypeError("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

class Contract(models.Model):
    _name = 'budget.contract'
    _rec_name = 'contract_no'
    _description = 'Contract'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'closed'], is_sorted=False)
    TYPES = choices_tuple(['principal', 'amendment', 'addendum'], is_sorted=False)
    VERSIONS = [(i, int_to_roman(i)) for i in range(1, 100)]
    SICET_TYPES = choices_tuple(['2a', '2b', '3'], is_sorted=False)
    SUB_SICET_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)
    SYSTEM_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)
    NETWORK_TYPES = choices_tuple(['test1', 'test2', 'test3'], is_sorted=False)


    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='active')

    contract_no = fields.Char(string="Contract No")
    amount = fields.Float(string='Contract Amount', digits=(32, 4), default=0.00)
    service_amount = fields.Float(string='Service Amount', digits=(32, 4), default=0.00)
    material_amount = fields.Float(string='Material Amount', digits=(32, 4), default=0.00)

    sicet_type = fields.Selection(SICET_TYPES)
    sub_sicet_type = fields.Selection(SUB_SICET_TYPES)
    system_type = fields.Selection(SYSTEM_TYPES)
    network_type = fields.Selection(NETWORK_TYPES)
    change_type = fields.Selection(TYPES, default='principal')
    version = fields.Selection(VERSIONS)

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    remarks = fields.Text(string='Remarks')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    contractor_id = fields.Many2one('res.partner', string='Contractor')

    # BUTTON ACTIONS / TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2close(self):
        self.state = 'closed'
