from odoo import api, fields, models


class ProductSpanish(models.Model):
    _inherit = 'product.template'
    spanish_name = fields.Char(string="Spanish Name")
