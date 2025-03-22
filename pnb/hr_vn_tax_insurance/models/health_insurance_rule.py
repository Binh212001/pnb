from odoo import models, fields

class HealthInsuranceRule(models.Model):
    _name = 'hr.health.insurance.rule'
    _description = 'Health Insurance Rule'

    name = fields.Char(string='Rule Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)