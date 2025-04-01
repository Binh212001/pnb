from odoo import models, fields, api

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    deduction_type = fields.Selection([
        ('standard', 'Standard Deduction'),
        ('disabled', 'Disabled Person Deduction'),
        ('family', 'Family Circumstance Deduction'),
    ], string="Deduction Type", required=True, default='standard') #Giảm trừ bản thân
    dependent_count = fields.Integer(string="Number of Dependents", default=0)