# -*- coding: utf-8 -*-
# from odoo import http


# class HrVnSalaryDeductions(http.Controller):
#     @http.route('/hr_vn_salary_deductions/hr_vn_salary_deductions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_vn_salary_deductions/hr_vn_salary_deductions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_vn_salary_deductions.listing', {
#             'root': '/hr_vn_salary_deductions/hr_vn_salary_deductions',
#             'objects': http.request.env['hr_vn_salary_deductions.hr_vn_salary_deductions'].search([]),
#         })

#     @http.route('/hr_vn_salary_deductions/hr_vn_salary_deductions/objects/<model("hr_vn_salary_deductions.hr_vn_salary_deductions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_vn_salary_deductions.object', {
#             'object': obj
#         })

