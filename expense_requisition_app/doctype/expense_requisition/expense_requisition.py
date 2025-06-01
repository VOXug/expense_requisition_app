# Copyright (c) 2025, Manus AI Agent and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.user import get_users_with_role

class ExpenseRequisition(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		amended_from: DF.Link | None
		attachments: DF.Attach | None
		currency: DF.Link | None
		department: DF.Link | None
		expense_date: DF.Date
		reason: DF.Text
		requester: DF.Link
		status: DF.Literal["Draft", "Submitted", "Manager Approved", "Finance Approved", "Paid", "Rejected", "Cancelled"]
		workflow_state: DF.Data | None
	# end: auto-generated types

	def validate(self):
		# Fetch department from employee if not set (though it's set to fetch_from and read_only)
		if self.requester and not self.department:
			self.department = frappe.db.get_value("Employee", self.requester, "department")

	# This function will be called on every update due to the hook
	# We check if the workflow_state has changed to trigger notifications
	def on_update_send_notifications(self):
		if self.flags.ignore_notification:
			return

		if self.get("__islocal") or not self.get("workflow_state"):
			return # Don't send notification for new docs or if workflow not started

		# Check if workflow state changed
		original_workflow_state = self.get_doc_before_save().workflow_state if self.get_doc_before_save() else None
		if original_workflow_state == self.workflow_state:
			return # State hasn't changed

		# Prepare notification context
		context = self.as_dict()
		context["requester_name"] = frappe.db.get_value("Employee", self.requester, "employee_name")
		context["doc_link"] = frappe.utils.get_link_to_form(self.doctype, self.name)

		recipients = []
		subject = ""
		message = ""

		if self.workflow_state == "Submitted":
			recipients = get_users_with_role("Expense Manager")
			subject = f"Expense Requisition {self.name} Submitted for Approval"
			message = f"Expense Requisition <a href='{context['doc_link']}'>{self.name}</a> for {self.get_formatted('amount')} has been submitted by {context['requester_name']} and requires your approval."
		elif self.workflow_state == "Manager Approved":
			recipients = get_users_with_role("Finance Approver")
			subject = f"Expense Requisition {self.name} Approved by Manager"
			message = f"Expense Requisition <a href='{context['doc_link']}'>{self.name}</a> has been approved by the manager and requires finance approval."
		elif self.workflow_state == "Finance Approved":
			recipients = get_users_with_role("Finance Approver") # Notify finance again, maybe for payment processing
			subject = f"Expense Requisition {self.name} Approved by Finance"
			message = f"Expense Requisition <a href='{context['doc_link']}'>{self.name}</a> has been approved by finance and is ready for payment."
		elif self.workflow_state == "Paid":
			recipients = [self.requester]
			subject = f"Expense Requisition {self.name} Marked as Paid"
			message = f"Your Expense Requisition <a href='{context['doc_link']}'>{self.name}</a> has been marked as paid."
		elif self.workflow_state == "Rejected":
			recipients = [self.requester]
			subject = f"Expense Requisition {self.name} Rejected"
			message = f"Your Expense Requisition <a href='{context['doc_link']}'>{self.name}</a> has been rejected. Please review and amend if necessary."

		if recipients and subject and message:
			frappe.sendmail(
				recipients=recipients,
				sender=frappe.session.user,
				subject=subject,
				message=message,
				doc=self,
				# template="expense_requisition_notification" # Optional: Use email template
			)


