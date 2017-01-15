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
        'budget_utilities',
        'budget_enduser'
    ],
    'data': [
        # SECURITY
        'security/budget_contractor.xml',
        'security/ir.model.access.csv',

        # VIEW
        'views/contract.xml',
        'views/contractor.xml',
        'views/rfs.xml',
        'views/milestone.xml',

        'views/menu.xml',

        # VIEW INHERIT
        'views/section_inherit.xml'
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
