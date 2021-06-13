from odoo import _

from odoo import api, fields, models
from datetime import datetime


class HospitalAppoinment(models.Model):
    _name = "hospital.appoinment"
    _description = "Hospital appoinment"
    patient_id = fields.Many2one('hospital.patient',
                                ondelete='set null', string='Patients Card', )

    # tocken_id = fields.Many2one(
    #     'hospital.ticket', ondelete='set null', string='OP', )
    tocken_no = fields.Char(string='Tocken Number', copy=False, readonly=True,
                            index=True, )
    name = fields.Char(string='Name', related='patient_id.patient_id.name', )
    doctor_id = fields.Many2one('hr.employee', ondelete='set null', string="Doctors")
    department_id = fields.Many2one(string="Department", related='doctor_id.department_id')
    date = fields.Date(string="Date" , default=datetime.today(), store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('op', 'OP'),
        ('app', 'Appoinment')

    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    op_count = fields.Integer(string='OP count', compute='_compute_get_op', readonly=True)

    @api.onchange('patient_id')
    def change_domain(self):
            return {'domain': {'doctor_id': [('job_title', '=', 'Doctor')]}}

    def action_confirm(self):
        self.state = 'app'
        tocken_op = self.env["hospital.ticket"].search_count(
            [('date', '=', self.date),
             ('doctor_id', '=', self.doctor_id.id),
             ('state', '=', 'op')])
        print("oppp", tocken_op)
        if tocken_op == 0:
            tocken = self.env["hospital.ticket"].search_count(
                [('date', '=', self.date),
                 ('doctor_id', '=', self.doctor_id.id),
                 ('state', '=', 'op')])
            tocken = tocken + 1
        else:
            tocken = tocken_op + 1

        self.tocken_no = "T" + str(tocken)

    def action_op(self):
        print("iddd", self.id)
        return {
            'name': _('OP'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.ticket',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def action_convert_op(self):

        self.state = 'op'
        _rec_name = 'op'
        print("iddd", self.id)
        return {
            'name': _('OP'),
            'view_type': 'form',
            'res_model': 'hospital.ticket',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'state': 'op',

        }

    # @api.onchange('patient_id')
    # def _onchange_change_domain(self):
    #
    #     for rec in self:
    #         print("recccc",rec)
    #         print("hereee", rec.patient_id)
    #         return {'domain': {'tocken_id': [('patient_id', '=', rec.patient_id.id)]}}

    @api.depends('patient_id')
    def _compute_get_op(self):
        op = self.env["hospital.appoinment"].search_count(
                [('date', '=', self.date),
                 ('doctor_id', '=', self.doctor_id.id),
                 ('state', '=', 'op')])

        self.op_count = op