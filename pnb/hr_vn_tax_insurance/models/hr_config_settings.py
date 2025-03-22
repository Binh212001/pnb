from email.policy import default

from odoo import models, fields, api


class HrConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_social_insurance = fields.Boolean(string='Enable Social Insurance')  # Bật/Tắt bảo hiểm xã hội
    enable_health_insurance = fields.Boolean(string='Enable Health Insurance')  # Bật/Tắt bảo hiểm y tế
    enable_unemployment_insurance = fields.Boolean(string='Enable Unemployment Insurance')  # Bật/Tắt bảo hiểm thất nghiệp