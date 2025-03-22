from odoo import models, fields

class SocialInsurance(models.Model):
    _name = 'hr.social.insurance'
    _description = 'Social Insurance Information'  # Thông tin bảo hiểm xã hội

    name = fields.Char(string='Insurance Name', required=True)  # Tên bảo hiểm
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')  # Nhân viên liên kết
    insurance_number = fields.Char(string='Insurance Number')  # Số sổ bảo hiểm
    start_date = fields.Date(string='Start Date')  # Ngày bắt đầu đóng bảo hiểm
    end_date = fields.Date(string='End Date')  # Ngày kết thúc bảo hiểm (nếu có)
    employee_contribution = fields.Monetary(string='Employee Contribution')  # Mức đóng của nhân viên
    employer_contribution = fields.Monetary(string='Employer Contribution')  # Mức đóng của doanh nghiệp
    total_paid_months = fields.Integer(string='Total Paid Months')  # Tổng số tháng đã đóng
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending')
    ], string='Status', default='active')  # Trạng thái bảo hiểm
    benefit_ids = fields.Many2many( 'hr.insurance.benefits', 'res_social_res_benefits_group_rel',
                                   'res_insurance_id', 'res_benefit_id', string="Benefits" )
    currency_id = fields.Many2one('res.currency', string='Currency')  # Loại tiền tệ
