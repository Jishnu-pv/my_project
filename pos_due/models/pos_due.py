from odoo import api, fields, models


class PosDue(models.Model):
    _inherit = 'res.partner'

    due_limit = fields.Char(String="Due Limit",)


    # def _compute_get_age(self):
    #     self.due_limit = self.amount_paid
    #     print("valuee is",self.due_limit)


