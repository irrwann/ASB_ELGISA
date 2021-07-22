# -*- coding: utf-8 -*-
# from odoo import http


# class AsbHelpdesk(http.Controller):
#     @http.route('/asb_helpdesk/asb_helpdesk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asb_helpdesk/asb_helpdesk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asb_helpdesk.listing', {
#             'root': '/asb_helpdesk/asb_helpdesk',
#             'objects': http.request.env['asb_helpdesk.asb_helpdesk'].search([]),
#         })

#     @http.route('/asb_helpdesk/asb_helpdesk/objects/<model("asb_helpdesk.asb_helpdesk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asb_helpdesk.object', {
#             'object': obj
#         })
