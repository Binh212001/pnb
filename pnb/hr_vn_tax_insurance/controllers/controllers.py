# -*- coding: utf-8 -*-
# from odoo import http


# class HrVnTaxInsurance(http.Controller):
#     @http.route('/hr_vn_tax_insurance/hr_vn_tax_insurance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_vn_tax_insurance/hr_vn_tax_insurance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_vn_tax_insurance.listing', {
#             'root': '/hr_vn_tax_insurance/hr_vn_tax_insurance',
#             'objects': http.request.env['hr_vn_tax_insurance.hr_vn_tax_insurance'].search([]),
#         })

#     @http.route('/hr_vn_tax_insurance/hr_vn_tax_insurance/objects/<model("hr_vn_tax_insurance.hr_vn_tax_insurance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_vn_tax_insurance.object', {
#             'object': obj
#         })

