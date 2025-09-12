import frappe
from erpnext.projects.doctype.task.task import Task

class CustomTask(Task):
    def validate(self):
        super().validate()
        frappe.log_error("My test message", "CustomTask Debug")

