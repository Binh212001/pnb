# -*- coding: utf-8 -*-

from odoo import models, fields, api , _
from odoo.exceptions import UserError


class HrAttendance(models.Model):
    _inherit = "hr.attendance"
    check_in = fields.Datetime(string="Check In",  required=False, tracking=True)

    @api.model
    def create(self, values):
        employee_id = values.get("employee_id")
        if employee_id:
            employee = self.env["hr.employee"].browse(employee_id)
            contract = employee.contract_id

            if not contract or contract.state in ["close", "cancel"]:
                raise UserError(_("Contract is closed or canceled. Cannot create attendance record."))

        return super(HrAttendance, self).create(values)

    @api.model
    def _cron_create_attendance_for_employee(self):
        employees = self.env["hr.employee"].search([])
        for emp in employees:
            contract = emp.contract_id
            if contract and contract.state not in ["close", "cancel"]:
                self.create({
                    "employee_id": emp.id,
                })


