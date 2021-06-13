# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
import json
import datetime
import io

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools import date_utils

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class HospitalReport(models.TransientModel):
    _name = "hospital.report"
    _description = "make hospital patients report"
    patient_id = fields.Many2one(
        'hospital.patient', ondelete='set null', string='Patients Card', )
    patient_name_id = fields.Many2one(string="Patient name", related="patient_id.patient_id")
    tocken_id = fields.Many2one('hospital.ticket', string="Tocken Number")
    from_date = fields.Date(String="From Date")
    to_date = fields.Date(string="To Date")
    doctor_id = fields.Many2one('hr.employee', ondelete='set null',
                             string="Doctors")
    department_id = fields.Many2one('hr.department', string='Department')
    diseases_id = fields.Many2one('hospital.consultation', string="Deseases")

    def create_report(self):
        print("helooi",self.read()[0])
        data = {
            'model': 'hospital.report',
            'form': self.read()[0]
        }
        print("data is",data)


        docids = self.env['hospital.ticket'].search([]).ids
        print("docss",docids)

        return self.env.ref(
            'hospital_management.action_patients_id_card').report_action(self, data=data)

    def print_xlsx(self):

        data = {
            'model': 'hospital.report',
            'form': self.read()[0]
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'hospital.report',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):

        patient_card = data['form']['patient_id']
        date_from = data['form']['from_date']
        date_to = data['form']['to_date']
        dr = data['form']['doctor_id']
        department = data['form']['department_id']
        diseases = data['form']['diseases_id']
        patient_name = data['form']['patient_name_id']
        if patient_card:
            patient_cards = patient_card[1]
            patient_name = patient_name[1]
        else:
            patient_cards = False
            patient_name = False
        if dr:
            drs = dr[1]
        else:
            drs = False

        if patient_card and date_from and date_to and dr and department and diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
            he.name as doctor,ht.date as date,
            hemp.name as department,hd.disease as diseases 
            from hospital_ticket ht
            INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
            INNER JOIN res_partner rs ON rs.id = hp.patient_id
            INNER JOIN hr_employee he ON ht.doctor_id = he.id
            INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
            INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
            INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

            WHERE hd.disease = '""" + str(diseases[1]) + """' 
            AND hemp.name = '""" + str(department[1]) + """' AND 
            hp.name = '""" + str(patient_card[1]) + """'  AND  
            ht.date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"'
                 and he.name = '""" + str(dr[1]) + """'

                """
        elif patient_card and date_from and date_to:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                        he.name as doctor,ht.date as date,
                        hemp.name as department,hd.disease as diseases 
                        from hospital_ticket ht
                        INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                        INNER JOIN res_partner rs ON rs.id = hp.patient_id
                        INNER JOIN hr_employee he ON ht.doctor_id = he.id
                        INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                        INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                        INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                WHERE hp.name = '""" + str(
                patient_card[1]) + """' and   ht.date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"' 

                """

        elif date_from and date_to:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                  INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                 INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                WHERE  ht.create_date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"' 

                             """

        elif patient_card:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                  he.name as doctor,ht.date as date,
                  hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                 INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                 INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                WHERE hp.name = '""" + str(patient_card[1]) + """' """
        elif diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                  he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                 INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

             WHERE   hd.diseases_id = '""" + str(diseases[1]) + """' """

        elif patient_card and dr and diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                 INNER JOIN hr_employee he ON ht.doctor_id = he.id
                  INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
                       WHERE   hd.diseases_id = '""" + str(
                diseases) + """' and hp.name = '""" + str(
                patient_card[1]) + """' and he.name = '""" + str(dr[1]) + """'
                    """
        elif dr:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                 he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                     WHERE   he.name = '""" + str(dr[1]) + """'
                                   """

        else:

            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,hemp.name as department,
                hd.disease as diseases  from 
                hospital_ticket ht 
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs  ON rs.id = hp.patient_id
                INNER JOIN hr_employee he  ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id"""
        self.env.cr.execute(q)
        docs = self.env.cr.dictfetchall()
        print(docs)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'font_size': '12px'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        th = workbook.add_format(
            {'bold': True, 'font_size': '10px',})
        td = workbook.add_format(
            {'font_size': '10px'})
        txt = workbook.add_format({'font_size': '10px'})
        sheet.merge_range('B2:I3', 'Medical REPORT', head)
        sheet.write('B6', 'From:', cell_format)
        sheet.merge_range('B4:C4', 'patient ID', th)
        sheet.merge_range('D4:E4', patient_cards, txt)
        sheet.merge_range('F4:G4', 'patient Name', th)
        sheet.merge_range('H4:I4', patient_name, txt)
        sheet.merge_range('B5:C5', 'Doctor Name', th)
        sheet.merge_range('D5:E5', drs, txt)
        sheet.merge_range('C6:D6', date_from, txt)
        sheet.write('F6', 'To:', cell_format)
        sheet.merge_range('G6:H6', date_to, txt)
        sheet.write(7, 1, 'sl No', th)
        sheet.write(7, 2, 'OP', th)
        sheet.write(7, 3, 'Patient Name', th)
        sheet.write(7, 4, '', th)
        sheet.write(7, 5, 'Date', th)
        sheet.write(7, 6, '', th)
        sheet.write(7, 7, 'Doctor', th)
        sheet.write(7, 8, 'Department', th)
        sheet.write(7, 9, '', th)
        sheet.write(7, 10, 'Diseases', th)

        rows = 8
        for rec in docs:
            sheet.write(rows, 1, rec['sl'], td)
            sheet.write(rows, 2, rec['tocken_no'], td)
            sheet.write(rows, 3, rec['name'], td)
            sheet.write(rows, 4, '', td)
            sheet.write(rows, 5, str(rec['date']), td)
            sheet.write(rows, 6, '', td)
            sheet.write(rows, 7, rec['doctor'], td)
            sheet.write(rows, 8, rec['department'], td)
            sheet.write(rows, 9, '', td)
            sheet.write(rows, 10, rec['diseases'], td)
            rows = rows+1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

    @api.onchange('patient_id')
    def change_domain(self):
        for rec in self:
            return {'domain': {'doctor_id': [('job_title', '=', 'Doctor')]}}



