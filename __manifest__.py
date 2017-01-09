# -*- coding: utf-8 -*-
{
    'name': "Contractor",
    'version': '0.1',
    'summary': 'Contractor Management',
    'sequence': 2,
    'description': """
Odoo Module
===========
Specifically Designed for Etisalat-TBPC

Contractor Management
---------------------
- Contract
- Contractor
- Contractor Contact
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': [
        'budget_enduser',
        'budget_core'
    ],
    'data': [
        # SECURITY
        'security/budget_contractor.xml',
        'security/ir.model.access.csv',

        'views/contract.xml',
        'views/contractor.xml',
        'views/menu.xml',

        # VIEW INHERIT
        'views/budget_inherit.xml'
    ],
    'demo': [
        'demo/res.partner.csv',
        'demo/budget.contract.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
