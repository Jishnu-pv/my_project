import datetime
from datetime import date

from AptUrl.Helpers import _

from odoo import api, fields, models


class Hospitals(models.Model):

    _name = "hospital.disease"
    _description = "Hospital patient"
    _rec_name = 'disease'
    disease = fields.Char(string='Disease ', required=True)
