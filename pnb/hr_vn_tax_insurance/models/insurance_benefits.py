from odoo import models, fields

class InsuranceBenefits(models.Model):
    _name = 'hr.insurance.benefits'
    _description = 'Insurance Benefits Information'  # Thông tin quyền lợi bảo hiểm

    name = fields.Char(string='Benefit Name', required=True)  # Tên quyền lợi
    description = fields.Text(string='Description')  # Mô tả chi tiết quyền lợi
    insurance_id = fields.Many2one('hr.social.insurance', string='Related Insurance', required=True, ondelete='cascade')  # Liên kết đến bảo hiểm xã hội
    eligibility_criteria = fields.Text(string='Eligibility Criteria')  # Điều kiện hưởng quyền lợi
    max_coverage = fields.Monetary(string='Maximum Coverage Amount')  # Số tiền bảo hiểm tối đa
    currency_id = fields.Many2one('res.currency', string='Currency')  # Loại tiền tệ
    active = fields.Boolean(string='Active', default=True)  # Trạng thái hoạt động
    insurance_type = fields.Selection([
        ('bhxh', 'Social Insurance (BHXH)'),
        ('bhyt', 'Health Insurance (BHYT)'),
        ('bhtn', 'Unemployment Insurance (BHTN)')
    ], string='Insurance Type', required=True)