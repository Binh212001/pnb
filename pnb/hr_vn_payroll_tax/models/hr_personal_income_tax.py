from odoo import models, fields


class HRPersonalIncomeTax(models.Model):
    _name = 'hr.personal.income.tax'
    _description = 'Personal Income Tax Information'  # Thông tin thuế thu nhập cá nhân

    name = fields.Char(string='Employee Name', required=True)  # Tên nhân viên
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,
                                  ondelete='cascade')  # Nhân viên liên kết
    tax_identification_number = fields.Char(string='Tax Identification Number')  # Mã số thuế cá nhân
    tax_bracket = fields.Selection([
        ('5', '5%'),
        ('10', '10%'),
        ('15', '15%'),
        ('20', '20%'),
        ('25', '25%'),
        ('30', '30%'),
        ('35', '35%')
    ], string='Tax Bracket')  # Bậc thuế suất

    taxable_income = fields.Monetary(string='Taxable Income')  # Thu nhập chịu thuế
    tax_amount = fields.Monetary(string='Tax Amount')  # Số tiền thuế phải nộp
    deductions = fields.Monetary(string='Deductions')  # Các khoản giảm trừ
    net_income = fields.Monetary(string='Net Income')  # Thu nhập sau thuế
    currency_id = fields.Many2one('res.currency', string='Currency')  # Loại tiền tệ
    notes = fields.Text(string='Notes')  # Ghi chú bổ sung
