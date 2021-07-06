from odoo import http
from odoo.http import content_disposition, request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website.controllers.main import QueryURL
import json
import logging



class Website(http.Controller):

    @http.route(
        ["/website_most_sold/products"],
        type='json', auth="public", website=True
    )
    def products(self, page=0, category=None, search='', ppg=False, **post):
     print("haii")
     v= request.env['website.track'].search([])
     print("heree visii",v.visitor_id)
     visitor = request.env['website.visitor']._get_visitor_from_request()
     print("visitor",visitor.product_ids)

     pricelist = request.website.get_current_pricelist()
     print("pricee",pricelist)
     print("check", request.env['product.product'].search([], order="sales_count desc"))
     print("check",
           request.env['product.template'].search([], order="sales_count desc"))
     print("check1111111111",
           request.env['product.product'].search([], order="most_viwed desc"))
     values = {
         'search': search,
         'category': category,
         'pricelist':pricelist

     }
     # return {
     #
     #     'output_data': output_data
     #
     # }
     #
     # return request.website.viewref(template).render({
     #     "object": categories,
     #     "keep": keep
     # })

     response = http.Response(template='website_most_sold.snippet_testimonial',
                              qcontext=values)
     return response.render()



     # return request.render("website_most_sold.snippet_testimonial", values)

     #res = super(WebsiteData1, self).shop(self)
     #return request.website.render({
     #return request.render("website_most_sold.snippet_testimonial", values)
     # categories = request.env["product.public.category"].search()
     # print("carrr",categories)
     # return  res

