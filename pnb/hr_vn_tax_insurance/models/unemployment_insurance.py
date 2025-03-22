from odoo import models, fields



class UnemploymentInsurance(models.Model):
    _name = 'hr.unemployment.insurance'
    _description = 'Unemployment Insurance Information'  # Thông tin bảo hiểm thất nghiệp

    name = fields.Char(string='Insurance Name', required=True)  # Tên bảo hiểm
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')  # Nhân viên
    contribution_rate = fields.Float(string='Contribution Rate (%)')  # Mức đóng BH thất nghiệp
    benefit_rate = fields.Float(string='Benefit Rate (%)')  # Mức hưởng BH thất nghiệp
    contribution_period = fields.Integer(string='Contribution Period (Months)')  # Thời gian đóng BH thất nghiệp
    benefit_duration = fields.Integer(string='Benefit Duration (Months)')  # Thời gian hưởng BH thất nghiệp
    allowance_amount = fields.Monetary(string='Unemployment Allowance Amount')  # Số tiền trợ cấp thất nghiệp
    start_date = fields.Date(string='Start Date')  # Ngày bắt đầu đóng bảo hiểm
    end_date = fields.Date(string='End Date')  # Ngày kết thúc đóng bảo hiểm
    insurance_number = fields.Char(string='Insurance Number')  # Số sổ bảo hiểm
    insurance_org = fields.Char(string='Insurance Organization')  # Tổ chức bảo hiểm
    history_ids = fields.One2many('hr.insurance.history', 'health_insurance_id',
                                  string='History of Hospital Visits') # Lịch sử đóng bảo hiểm
    termination_reason = fields.Text(string='Termination Reason')  # Lý do chấm dứt bảo hiểm
    active = fields.Boolean(string='Active', default=True)  # Trạng thái hoạt động
    benefit_ids = fields.Many2many('hr.insurance.benefits', 'res_unemployment_res_benefits_group_rel',
                                   'res_insurance_id', 'res_benefit_id', string="Benefits")

    currency_id = fields.Many2one('res.currency', string='Currency')  # Loại tiền tệ
