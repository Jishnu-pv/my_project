from odoo import api, fields, models
from datetime import datetime


class webDetails(models.Model):
    _name = 'web.details'

    review = fields.Text(string="Review")
    rating = fields.Char(string="Rating")
    ratings = fields.Char(string="Rating")
    cust = fields.Char(string="customer")
    #date = fields.Date(string="Date" , default=datetime.today(), store=True)
    date = fields.Datetime('Date current action', required=False,
                                  readonly=False, select=True
                                  , default=lambda self: fields.datetime.now())
    # product_id = fields.Many2one('product.product', ondelete='set null',
    #                              string="Product ID", store=True)
    product_id=fields.Integer(string="ID")
    avg = fields.Char(string="Average")

    @api.model
    def getdata(self, docids, data=None):
        q = """select * from web.details"""
        self.env.cr.execute(q)
        docs = self.env.cr.dictfetchall()
        # print("kkkk>>>", docs[0])
        # print("here docss", q)
        print("here docss", docs)

