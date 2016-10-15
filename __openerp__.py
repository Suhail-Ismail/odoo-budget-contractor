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
    'depends': ['base','mail'],
    'data': [
        'views/contractor.xml',
        'views/contract.xml',
        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
