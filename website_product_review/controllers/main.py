from odoo import http
from odoo.http import content_disposition, request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteData(WebsiteSale):
    @http.route('/create/data', type="http", auth="public", website=True)
    def create_data(self, **kwargs):
        avg = 0
        print("self",self)
        print("here",kwargs)
        print("haha")

        cust = request.env.user.name
        productreview = request.env['web.details'].sudo().create({
            'review':kwargs.get('review'),
            'ratings':kwargs.get('ratings'),
            'cust':cust,
            'avg':avg,
            'product_id':kwargs.get('product_id')
        })

        print("ratingss",productreview.ratings)
        print("product", productreview.rating)




        print("name",cust)

        return request.redirect(request.httprequest.referrer)
        #return request.render("website_product_review.product_review",values)

        # response = http.request.render('website_product_review.product_review', {
        #     'context_value': 42
        # })

        # @http.route(['/shop/<model("web.details"):product>'], type='http',
        #             auth="public", website=True, sitemap=True)
        #
        # def product(self, product, category='', search='', **kwargs):
        #     return request.render("website_sale.product",
        #                           self._prepare_product_values(product,
        #                                                        category, search,
        #                                                        **kwargs))

        # MealType = http.request.env['product.template']
        # print("hreredatas",MealType.review)


        #return request.render("website_sale.product")

        #rating = request.website.viewref('web.details.review').active
        # print("heree",rating)



    # @http.route([
    #     '''/shop''',
    #     '''/shop/page/<int:page>''',
    #     '''/shop/category/<model("product.public.category"):category>''',
    #     '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    # ], type='http', auth="user", website=True)
    # def shop(self,  **kwargs):
    #     print("heree",kwargs)
    #     res = super(WebsiteData, self).shop(self,  **kwargs)
    #     print("haiiihello", kwargs.get('review'))
    #     productreview = request.env['web.details'].sudo().create({
    #
    #         'review':kwargs.get('review'),
    #         'rating':kwargs.get('rating'),
    #
    #     })
    #     print("product",productreview)
    #     # if productreview:
    #     #     print("y")
    #     # print("product",productreview.rev)
    #     # vals = {
    #     #     'review':productreview,
    #     #     'rating':productreview
    #     # }
    #
    #     # print("haii", vals['review'])
    #     # print("he")
    #
    #     return res



    # @http.route(['/shop/<model("product.template"):product>'], type='http',auth="public", website=True)
    # def product(self, product, category='', search='', review='', **kwargs):
    #     res = super(WebsiteData, self).product(product, category='', search='', review='', **kwargs)
    #     print("Inherited ....", res.qcontext)
    #     return res




# import werkzeug
#
# from werkzeug.exceptions import NotFound, Forbidden
#
# from odoo import http
# from odoo.http import request
# from odoo.addons.portal.controllers.mail import _check_special_access, PortalChatter
# from odoo.tools import plaintext2html, html2plaintext
#
#
# class WebsiteDetails(PortalChatter):
#      @http.route(['/mail/chatter_post'], type='http', methods=['POST'], auth='public', website=True)
#     def portal_chatter_post(self, res_model, res_id, message, **kw):
#         result = super(WebsiteDetails, self).portal_chatter_post(self, res_model, res_id, message, **kw)
#         print("haii")
#         return result



