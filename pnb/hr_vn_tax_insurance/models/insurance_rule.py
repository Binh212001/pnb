from odoo import models, fields

class InsuranceRule(models.Model):
    _name = 'hr.insurance.rule'
    _description = 'Health Insurance Rule'

    name = fields.Char(string='Rule Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)