# -*- coding: utf-8 -*-
# from odoo import http


# class RentalCustomization(http.Controller):
#     @http.route('/rental_customization/rental_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rental_customization/rental_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rental_customization.listing', {
#             'root': '/rental_customization/rental_customization',
#             'objects': http.request.env['rental_customization.rental_customization'].search([]),
#         })

#     @http.route('/rental_customization/rental_customization/objects/<model("rental_customization.rental_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rental_customization.object', {
#             'object': obj
#         })

