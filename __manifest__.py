# -*- coding: utf-8 -*-
{
    'name': "Contractor",
    'version': '0.1',
    'summary': 'Contractor Management',
    'sequence': 2,
    'description': """
Odoo Module
-----------

Specifically Designed for Etisalat-TBPC

Contractor Management
---------------------

- Contract
- Contractor
- Contractor Contact
- Ready for Service
- Milestone
- Section Inherit
- Access Users
        - Dependent - Can readonly
        - User - General Usage except delete power, can Edit recurrence but not create
        - Manager - All power to manipulate data

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
        'views/contractor_contact.xml',
        'views/rfs.xml',
        'views/milestone.xml',
        'views/system_type.xml',

        # VIEW INHERIT
        'views/milestone_inherit_actual.xml',
        'views/rfs_inherit_actual.xml',
        # 'views/section_inherit.xml',

        'views/menu.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
