# -*- coding: utf-8 -*-
# from odoo import http


# class HrVnPayrollTax(http.Controller):
#     @http.route('/hr_vn_payroll_tax/hr_vn_payroll_tax', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_vn_payroll_tax/hr_vn_payroll_tax/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_vn_payroll_tax.listing', {
#             'root': '/hr_vn_payroll_tax/hr_vn_payroll_tax',
#             'objects': http.request.env['hr_vn_payroll_tax.hr_vn_payroll_tax'].search([]),
#         })

#     @http.route('/hr_vn_payroll_tax/hr_vn_payroll_tax/objects/<model("hr_vn_payroll_tax.hr_vn_payroll_tax"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_vn_payroll_tax.object', {
#             'object': obj
#         })

