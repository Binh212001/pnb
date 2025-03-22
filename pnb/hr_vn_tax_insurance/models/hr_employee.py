from odoo import models, fields, api

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    social_insurance_id = fields.Many2one('hr.social.insurance', string='Social Insurance')  # Liên kết đến bảo hiểm xã hội
    health_insurance_id = fields.Many2one('hr.health.insurance', string='Health Insurance')  # Liên kết đến bảo hiểm y tế
    unemployment_insurance_id = fields.Many2one('hr.unemployment.insurance', string='Unemployment Insurance')  # Liên kết đến bảo hiểm thất nghiệp

