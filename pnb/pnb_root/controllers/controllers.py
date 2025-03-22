# -*- coding: utf-8 -*-
# from odoo import http


# class PnbRoot(http.Controller):
#     @http.route('/pnb_root/pnb_root', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pnb_root/pnb_root/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pnb_root.listing', {
#             'root': '/pnb_root/pnb_root',
#             'objects': http.request.env['pnb_root.pnb_root'].search([]),
#         })

#     @http.route('/pnb_root/pnb_root/objects/<model("pnb_root.pnb_root"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pnb_root.object', {
#             'object': obj
#         })

