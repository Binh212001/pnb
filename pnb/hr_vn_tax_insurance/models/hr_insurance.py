from odoo import models, fields


class Insurance(models.Model):
    _name = 'hr.insurance'
    _description = 'Insurance Information'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')
    name = fields.Char(string='Insurance Name', required=True)
    insurance_number = fields.Char(string='Insurance Number')
    insurance_type = fields.Selection([
        ('health', 'Health Insurance'),
        ('social', 'Social Insurance'),
        ('unemployment', 'Unemployment Insurance')
    ], string='Insurance Type', required=True)

    # Common Fields
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    currency_id = fields.Many2one('res.currency', string='Currency')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
        ('suspended', 'Suspended')
    ], string='Status', default='active')

    # Health Insurance Specific Fields
    registered_hospital = fields.Char(string='Registered Hospital')
    issue_date = fields.Date(string='Issue Date')
    expiry_date = fields.Date(string='Expiry Date')
    coverage_rate = fields.Float(string='Coverage Rate (%)')
    contribution_rate = fields.Float(string='Contribution Rate (%)')
    max_coverage_limit = fields.Monetary(string='Maximum Coverage Limit')
    annual_claims = fields.Monetary(string='Annual Claims Amount')
    maternity_support = fields.Boolean(string='Maternity Support')
    extended_benefits = fields.Text(string='Additional Benefits')
    related_social_insurance = fields.Boolean(string='Linked with Social Insurance')
    history_ids = fields.One2many('hr.insurance.history', 'insurance_id', string='History of Hospital Visits')
    policy_rules = fields.Many2many('hr.health.insurance.rule', string='Policy Rules')

    # Social Insurance Specific Fields
    total_paid_months = fields.Integer(string='Total Paid Months')
    employee_contribution = fields.Monetary(string='Employee Contribution')
    employer_contribution = fields.Monetary(string='Employer Contribution')
    benefit_ids = fields.Many2many('hr.insurance.benefits', 'res_insurance_res_benefits_group_rel',
                                   'res_insurance_id', 'res_benefit_id', string="Benefits")

    # Unemployment Insurance Specific Fields
    contribution_period = fields.Integer(string='Contribution Period (Months)')
    benefit_duration = fields.Integer(string='Benefit Duration (Months)')
    allowance_amount = fields.Monetary(string='Unemployment Allowance Amount')
    insurance_org = fields.Char(string='Insurance Organization')
    termination_reason = fields.Text(string='Termination Reason')
