from odoo import models, fields, api


class HRVnSalaryDeductions(models.Model):
    _name = "hr.vn.salary.deductions"
    _description = "Vietnam Salary Deductions"

    name = fields.Char(string="Deduction Name", required=True)
    deduction_type = fields.Selection([
        ('bhxh', 'Bảo hiểm xã hội (BHXH)'),
        ('bhyt', 'Bảo hiểm y tế (BHYT)'),
        ('bhtn', 'Bảo hiểm thất nghiệp (BHTN)'),
        ('tncn', 'Thuế thu nhập cá nhân (TNCN)'),
        ('other', 'Khấu trừ khác')
    ], string="Deduction Type", required=True)

    amount = fields.Float(string="Deduction Amount", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    @api.onchange('deduction_type')
    def _compute_deduction_amount(self):
        """Tự động cập nhật mức khấu trừ dựa trên loại bảo hiểm"""
        if self.deduction_type == 'bhxh':
            self.amount = 8  # Ví dụ: BHXH 8% lương
        elif self.deduction_type == 'bhyt':
            self.amount = 1.5  # Ví dụ: BHYT 1.5% lương
        elif self.deduction_type == 'bhtn':
            self.amount = 1  # Ví dụ: BHTN 1% lương
