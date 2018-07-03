# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    "author": "Grant Thornton S.L.P.",
    "website": 'http://www.grantthornton.es/',

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/reports.xml',
        'views/session_board.xml',
        'wizard/openacademy_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'views/demo.xml',
    ],
}
