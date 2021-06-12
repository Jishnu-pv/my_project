# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS spanish',
    'version': '1.0',
    'category': 'Productivity',
    'description': "POS Spanish Name",
    'summary': '',
    'sequence': 260,
     'qweb': ['static/src/xml/receipt_pos.xml','static/src/xml/spanish_pos.xml'],
    'depends': ['base', 'contacts', 'hr', 'base', 'web','account','sale'],
"external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    'data': ['views/spanish_name.xml','views/action_manager.xml'],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
