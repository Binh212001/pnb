# -*- coding: utf-8 -*-
# from odoo import http


# class HrAttendance(http.Controller):
#     @http.route('/hr_attendance/hr_attendance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_attendance/hr_attendance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_attendance.listing', {
#             'root': '/hr_attendance/hr_attendance',
#             'objects': http.request.env['hr_attendance.hr_attendance'].search([]),
#         })

#     @http.route('/hr_attendance/hr_attendance/objects/<model("hr_attendance.hr_attendance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_attendance.object', {
#             'object': obj
#         })

