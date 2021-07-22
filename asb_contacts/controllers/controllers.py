# -*- coding: utf-8 -*-
# from odoo import http


# class AsbContacts(http.Controller):
#     @http.route('/asb_contacts/asb_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asb_contacts/asb_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asb_contacts.listing', {
#             'root': '/asb_contacts/asb_contacts',
#             'objects': http.request.env['asb_contacts.asb_contacts'].search([]),
#         })

#     @http.route('/asb_contacts/asb_contacts/objects/<model("asb_contacts.asb_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asb_contacts.object', {
#             'object': obj
#         })
