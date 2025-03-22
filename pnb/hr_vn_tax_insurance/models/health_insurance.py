from odoo import models, fields


class HealthInsurance(models.Model):
    _name = 'hr.health.insurance'
    _description = 'Health Insurance Information'

    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')
    name = fields.Char(related = "employee_id.name", required=True)
    insurance_number = fields.Char(string='Insurance Number', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender' ,related = "employee_id.gender" )
    birth_date = fields.Date(related = 'employee_id.birthday', string='Date of Birth' )
    hometown = fields.Char(string='Hometown')

    insurance_type = fields.Selection([
        ('mandatory', 'Mandatory'),
        ('voluntary', 'Voluntary')
    ], string='Insurance Type', required=True)
    registered_hospital = fields.Char(string='Registered Hospital')
    issue_date = fields.Date(string='Issue Date')
    expiry_date = fields.Date(string='Expiry Date')
    coverage_rate = fields.Float(string='Coverage Rate (%)')
    contribution_rate = fields.Float(string='Contribution Rate (%)')
    base_salary = fields.Monetary(string='Base Salary for Contribution')
    max_coverage_limit = fields.Monetary(string='Maximum Coverage Limit')
    insurance_status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('suspended', 'Suspended')
    ], string='Status', default='active')

    history_ids = fields.One2many('hr.insurance.history', 'health_insurance_id',
                                  string='History of Hospital Visits')
    annual_claims = fields.Monetary(string='Annual Claims Amount')
    policy_rules = fields.Many2many('hr.health.insurance.rule', string='Policy Rules')
    related_social_insurance = fields.Boolean(string='Linked with Social Insurance')
    maternity_support = fields.Boolean(string='Maternity Support')
    extended_benefits = fields.Text(string='Additional Benefits')

    currency_id = fields.Many2one('res.currency', string='Currency')
