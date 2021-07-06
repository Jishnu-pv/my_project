# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Snippets Most Sold Products',
    'version': '1.0',
    'category': 'Productivity',
    'description': "Website Snippets Most Sold Products",
    'summary': '',
    'sequence': 260,
     'qweb': [],
    'depends': ['base', 'contacts', 'hr', 'base', 'web','account','sale'],
"external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    'data': ['views/snippet.xml','views/template.xml'],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}