
from odoo import models, fields
class InsuranceHistory(models.Model):
    _name = 'hr.insurance.history'
    _description = 'Health Insurance History'

    health_insurance_id = fields.Many2one('hr.health.insurance', string='Health Insurance', required=True, ondelete='cascade')
    visit_date = fields.Date(string='Visit Date', required=True)
    hospital_name = fields.Char(string='Hospital Name', required=True)
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment Provided')
