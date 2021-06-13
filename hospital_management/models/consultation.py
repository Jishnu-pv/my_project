from AptUrl.Helpers import _

from odoo import api, fields, models
import datetime


class HospitalConsultation(models.Model):
    _name = "hospital.consultation"
    _rec_name = "disease_id"
    _description = "Hospital Op"
    patient_id = fields.Many2one(
        'hospital.patient', ondelete='set null', string='Patients Card', )
    con_id = fields.Selection([('o', 'OP'), ('i', 'IP'), ], string="Consultation Type")
    tocken_id = fields.Many2one(
        'hospital.ticket', ondelete='set null', string='Consultation Type', )
    #tocken_no = fields.Char(string='Tocken Number', related='patient_card.tocken_no')
    doctor_id = fields.Many2one(string="Doctor", related='tocken_id.doctor_id')
    department_id = fields.Many2one(string="Department", related='doctor_id.department_id', store=True)
    date = fields.Date(string="Date", compute='calculate_date')
    disease_id = fields.Many2one('hospital.disease', string='Disease')
    Diagnose = fields.Text(string="Diagnose")
    appoinment_line = fields.One2many('hospital.line', 'cons_id', ondelete='set null')

    @api.depends("patient_id")
    def calculate_date(self):
        today_date = datetime.date.today()
        self.date = today_date
        print("today", today_date)

    @api.onchange('patient_id')
    def change_domain(self):
        for rec in self:
            print("hereee", rec.patient_id)
            return {'domain': {'tocken_id': [('patient_id', '=', rec.patient_id.id)]}}


class HospitalConsultationLines(models.Model):
    _name = "hospital.line"
    _description = "Hospital Op"

    patient_id = fields.Many2one(
        'hospital.ticket', ondelete='set null', string='Patients Card', )

    medicine = fields.Text(string='Medicine')
    dose = fields.Char(string='Dose')
    days = fields.Integer(string='Days')
    description = fields.Char(string='Description')
    cons_id = fields.Many2one('hospital.consultation', string='consult_id')





class Hospital(models.Model):
    _name = "desease.patient"
    _rec_name = 'disease'
    _description = "Hospital patient"
    disease = fields.Char(string='disease ', required=True)