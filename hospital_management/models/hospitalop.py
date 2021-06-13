from AptUrl.Helpers import _

from odoo import api, fields, models
from datetime import datetime


class HospitalOpTicket(models.Model):
    _name = "hospital.ticket"
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin']
    _description = "Hospital Op"
    _rec_name = 'op'

    patient_id = fields.Many2one(
        'hospital.patient', ondelete='set null', string='Patients Card', )
    op = fields.Char(string='OP Reference', required=True, copy=False,
                       readonly=True,
                       index=True, default=lambda self: _('New'))
    #_patients_name = fields.Many2one("hr.employee.base", string="names")
    name = fields.Char(string='Name', related='patient_id.patient_id.name', )
    age = fields.Integer(string="Age", related='patient_id.age')
    dob = fields.Date(string="DOB", related='patient_id.dob')
    gender = fields.Selection(string="Gender", related="patient_id.gender")
    blood_group = fields.Selection(string="Blood Group", related="patient_id.blood_group")
    doctor_id = fields.Many2one('hr.employee', ondelete='set null', string="Doctors", store=True)
    department_id = fields.Many2one(string="Department", related='doctor_id.department_id', store=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency", related='company_id.currency_id', readonly=True)
    job = fields.Char(string="Gender", related="doctor_id.job_title")
    date = fields.Date(string="Date" , default=datetime.today(), store=True)
    tocken_no = fields.Char(string='Tocken Number', copy=False, readonly=True, index=True,)
    fee = fields.Integer(string='Fee', currency_field='currency_id', related='doctor_id.fee')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('op', 'OP'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    @api.model
    def create(self, vals):
        print("doctorr",self.doctor_id.id)
        print("self iss",self)

        if vals.get('op', _('New')) == _('New'):
            vals['op'] = self.env['ir.sequence'].next_by_code(
                  'hospital.sequence.op.no', ) or _('New')
        result = super(HospitalOpTicket, self).create(vals)
        print("here valss",vals)
        return result

    # @api.model
    # def create(self, vals):
    #     print("haii", vals)
    #     if vals.get('op', _('New')) == _('New'):
    #         vals['op'] = self.env['ir.sequence'].next_by_code(
    #             'hospital.sequence.op.no', ) or _('New')
    #     result = super(HospitalOpTicket, self).create(vals)
    #     return result

    print(op)

    def action_confirm(self):
        tocken_appoinemnt = self.env["hospital.appoinment"].search_count(
            [('date', '=', self.date),
             ('doctor_id', '=', self.doctor_id.id),
             ('state', '=', 'op')])
        if (tocken_appoinemnt == 0):
            tocken = self.env["hospital.ticket"].search_count(
                [('date', '=', self.date),
                 ('doctor_id', '=', self.doctor_id.id),
                 ('state', '=', 'op')])
            tocken = tocken + 1
        else:
            tocken = tocken_appoinemnt + 1

        self.tocken_no = "T" + str(tocken)
        print("t is", tocken)
        print("current doctor",self.doctor_id)
        self.state = 'op'

    @api.onchange('tocken_no')
    def change_domain(self):
            return {'domain': {'doctor_id': [('job_title', '=', 'Doctor')]}}

    def action_register_payment(self):
        ''' Open the account.payment.register wizard to pay the selected journal entries.
        :return: An action opening the account.payment.register wizard.
        '''
        return {
            'name': _('Register Payment'),
            'res_model': 'fee.payment.register',
            'view_mode': 'form',
            'context': {
                'active_model': 'hospital.ticket',
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    def create_invoice(self):
        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.patient_id,
            'invoice_date': self.date,
            'invoice_line_ids': [(0, 0, {
                'price_unit': self.fee

            })]
        }
        inv = self.env['account.move'].create(invoice_vals)
        return {
            'name': _('Register Payment'),
            'res_model': 'account.move',
            'target': 'new',
            'res_id': inv.id,
            'view-type': 'form',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            }



class HospitalOpTicket1(models.Model):
    _inherit = 'hospital.ticket'
    _name = "hospital.op"
    _description = "Hospital Op"
    _rec_name = 'tocken_no'