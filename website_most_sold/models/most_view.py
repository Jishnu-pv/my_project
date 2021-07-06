from datetime import timedelta, time
from odoo import api, fields, models
from odoo.tools.float_utils import float_round

class MostView(models.Model):

    _inherit = 'product.product'
    # most_count = fields.Float(compute='_compute_most_count', string='most',
    #                            store=True)
    most_viwed = fields.Integer(compute='_compute_most_count', string="most", store=True)

    def _compute_most_count(self):
        for rec in self:
            count = rec.env["website.track"].search_count([('product_id', '=', rec.id)])
            print("count iss",count)
            rec.most_viwed = count
