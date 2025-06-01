# -*- coding: utf-8 -*-
from . import __version__ as app_version

app_name = "expense_requisition_app"
app_title = "Expense Requisition App"
app_publisher = "Manus AI Agent"
app_description = "Custom ERPNext app for managing expense requisitions."
app_email = "support@example.com"
app_license = "MIT"
# app_logo_url = "/assets/expense_requisition_app/images/logo.png" # Optional: Add a logo later

# Includes in <head>
# ------------------

# app_include_css = "/assets/expense_requisition_app/css/expense_requisition_app.css"
# app_include_js = "/assets/expense_requisition_app/js/expense_requisition_app.js"
# web_include_css = "/assets/expense_requisition_app/css/expense_requisition_app.css"
# web_include_js = "/assets/expense_requisition_app/js/expense_requisition_app.js"
# website_theme_scss = "expense_requisition_app/public/scss/website"
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}
# page_js = {"page" : "public/js/file.js"}
# doctype_js = {"Expense Requisition" : "public/js/expense_requisition.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
# app_include_icons = "expense_requisition_app/public/icons.svg"

# Home Pages
# ----------
# home_page = "login"
# role_home_page = {"Role": "home_page"}

# Generators
# ----------
# website_generators = ["Web Page"]

# Jinja
# -----------
# jinja = {"methods": "expense_requisition_app.utils.jinja_methods", "filters": "expense_requisition_app.utils.jinja_filters"}

# Installation / Uninstallation
# -----------------------------
# before_install = "expense_requisition_app.install.before_install"
# after_install = "expense_requisition_app.install.after_install"
# before_uninstall = "expense_requisition_app.uninstall.before_uninstall"
# after_uninstall = "expense_requisition_app.uninstall.after_uninstall"

# Integration Setup / Cleanup
# ---------------------------
# before_app_install = "expense_requisition_app.utils.before_app_install"
# after_app_install = "expense_requisition_app.utils.after_app_install"
# before_app_uninstall = "expense_requisition_app.utils.before_app_uninstall"
# after_app_uninstall = "expense_requisition_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
notification_config = "expense_requisition_app.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions"}
# has_permission = {"Event": "frappe.desk.doctype.event.event.has_permission"}

# DocType Class
# ---------------
# override_doctype_class = {"ToDo": "custom_app.overrides.CustomToDo"}

# Document Events
# ----------------
doc_events = {
	"Expense Requisition": {
		"on_update": "expense_requisition_app.expense_requisition.on_update_send_notifications",
		# "on_submit": "expense_requisition_app.expense_requisition.on_submit_handler", # Use on_update for workflow changes
		# "on_cancel": "expense_requisition_app.expense_requisition.on_cancel_handler"
	}
}

# Scheduled Tasks
# ---------------
# scheduler_events = {
#	"all": ["expense_requisition_app.tasks.all"],
#	"daily": ["expense_requisition_app.tasks.daily"],
#	"hourly": ["expense_requisition_app.tasks.hourly"],
#	"weekly": ["expense_requisition_app.tasks.weekly"],
#	"monthly": ["expense_requisition_app.tasks.monthly"],
# }

# Testing
# -------
# before_tests = "expense_requisition_app.install.before_tests"

# Overriding Methods
# -------------------
# override_whitelisted_methods = {"frappe.desk.doctype.event.event.get_events": "expense_requisition_app.event.get_events"}
# override_doctype_dashboards = {"Task": "expense_requisition_app.task.get_dashboard_data"}

# ignore_links_on_cancel = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["expense_requisition_app.utils.before_request"]
# after_request = ["expense_requisition_app.utils.after_request"]

# Job Events
# -----------
# before_job = ["expense_requisition_app.utils.before_job"]
# after_job = ["expense_requisition_app.utils.after_job"]

# User Data Protection
# ---------------------
# user_data_fields = [
#	{"doctype": "{doctype_name}", "filter_by": "{filter_by}", "redact_fields": ["{field_1}", "{field_2}"], "partial": 1}
# ]

# Authentication and authorization
# --------------------------------
# auth_hooks = ["expense_requisition_app.auth.validate"]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {"Logging DocType Name": 30}

fixtures = [
    {"dt": "Workflow", "filters": [["name", "=", "Expense Requisition Workflow"]]}, # Use '=' for exact match
    {"doctype": "Custom Role", "filters": [["name", "in", ["Expense Manager", "Finance Approver"]]]} # Export custom roles
    # Workflow State and Action Master are usually handled automatically when exporting Workflow
]

