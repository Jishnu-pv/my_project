# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS Due Limit',
    'version': '1.0',
    'category': 'Productivity',
    'description': "POS Due Limit",
    'summary': '',
    'sequence': 260,
     'qweb': [],
    'depends': ['base', 'contacts', 'hr', 'base', 'web','account','sale'],
"external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    'data': ['views/pos_due.xml','views/action_manger.xml'],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
