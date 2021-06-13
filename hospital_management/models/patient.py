# -*- coding: utf-8 -*-
import random
import datetime
from datetime import date

from odoo import _

from odoo import api, fields, models


class Hospital(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin']
    _description = "Hospital patient"

    order_lines = fields.One2many('hospital.ticket', 'patient_id', ondelete='set null')

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(
        'res.partner', ondelete='set null', string='Patients Name', )

    dob = fields.Date(string="DOB", related='patient_id.dob')
    age = fields.Integer(string="Age",compute='_compute_get_age')
    gender = fields.Selection([('m', 'Male'), ('f', 'female'), ], string="Gender")
    mobile = fields.Char(string='mobile', related='patient_id.phone', )
    telephone = fields.Char(string='Telephone', related='patient_id.phone')
    blood_group = fields.Selection([
        ('b+', 'B+'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Group")

    #order_lines = fields.One2many('op.line', 'cons_id', ondelete='set null')

    @api.model
    def create(self, vals):
        print("haii", vals)
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.sequence.patient', ) or _('New')
        result = super(Hospital, self).create(vals)
        return result

    @api.depends("dob")
    def _compute_get_age(self):
        self.age = 0
        today_date = datetime.date.today()
        for stud in self:
            if stud.dob:
                dob = fields.Datetime.to_datetime(stud.dob).date()
                # now = dob1.year
                age = (today_date - dob).days / 365
                stud.age = age




