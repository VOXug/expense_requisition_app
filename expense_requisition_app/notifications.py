# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

def get_notification_config():
    """Returns notification settings for the app."""
    return {
        "for_doctype": {
            "Expense Requisition": {
                "workflow_state": [
                    {
                        "condition": "doc.workflow_state == \"Submitted\"",
                        "subject": "Expense Requisition {name} Submitted for Approval",
                        "message": "Expense Requisition {name} for {amount} {currency} has been submitted by {requester_name} and requires your approval.",
                        "recipients": "get_manager_approvers"
                    },
                    {
                        "condition": "doc.workflow_state == \"Manager Approved\"",
                        "subject": "Expense Requisition {name} Approved by Manager",
                        "message": "Expense Requisition {name} has been approved by the manager and requires finance approval.",
                        "recipients": "get_finance_approvers"
                    },
                    {
                        "condition": "doc.workflow_state == \"Finance Approved\"",
                        "subject": "Expense Requisition {name} Approved by Finance",
                        "message": "Expense Requisition {name} has been approved by finance and is ready for payment.",
                        "recipients": "get_finance_approvers"
                    },
                    {
                        "condition": "doc.workflow_state == \"Paid\"",
                        "subject": "Expense Requisition {name} Marked as Paid",
                        "message": "Expense Requisition {name} has been marked as paid.",
                        "recipients": "doc.requester"
                    },
                    {
                        "condition": "doc.workflow_state == \"Rejected\"",
                        "subject": "Expense Requisition {name} Rejected",
                        "message": "Expense Requisition {name} has been rejected. Please review and amend if necessary.",
                        "recipients": "doc.requester"
                    }
                ]
            }
        }
    }

def get_manager_approvers(doc):
    """Returns a list of users with the 'Expense Manager' role."""
    # In a real scenario, this might involve checking department managers, etc.
    # For simplicity, returning all users with the role.
    return frappe.get_users_with_role("Expense Manager")

def get_finance_approvers(doc):
    """Returns a list of users with the 'Finance Approver' role."""
    return frappe.get_users_with_role("Finance Approver")

