# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Productivity',
    'description': "Hospital management",
    'summary': '',
    'sequence': 260,
    'depends': ['base', 'contacts', 'hr', 'base', 'web','account','sale'],
"external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    'data': ['security/ir.model.access.csv',
             'views/patient.xml', 'wizards/make_report.xml', 'views/op.xml', 'data/sequence.xml', 'views/contactdob.xml', 'views/consultation.xml', 'views/appoinment.xml', 'report/hospital_report.xml','report/report_all_channels_patients.xml', 'views/desease.xml','views/action_manager.xml'],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
