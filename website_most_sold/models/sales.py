from datetime import timedelta, time
from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = 'product.template'

    sales_count = fields.Float(compute='_compute_sales_count', string='Sold', store=True)

    # sales_count1 = fields.Float(compute='_compute_sales_count1', string='Sold',
    #                             store=True)
    #
    # def _compute_sales_count1(self):
    #     r = {}
    #     self.sales_count1 = 0
    #     if not self.user_has_groups('sales_team.group_sale_salesman'):
    #         return r
    #     date_from = fields.Datetime.to_string(fields.datetime.combine(fields.datetime.now() - timedelta(days=365),
    #                                                                   time.min))
    #
    #     done_states = self.env['sale.report']._get_done_states()
    #
    #     domain = [
    #         ('state', 'in', done_states),
    #         ('product_id', 'in', self.ids),
    #         ('date', '>=', date_from),
    #     ]
    #     for group in self.env['sale.report'].read_group(domain, ['product_id', 'product_uom_qty'], ['product_id']):
    #         r[group['product_id'][0]] = group['product_uom_qty']
    #     for product in self:
    #         if not product.id:
    #             product.sales_count1 = 0.0
    #             continue
    #         product.sales_count1 = float_round(r.get(product.id, 0), precision_rounding=product.uom_id.rounding)
    #     return r