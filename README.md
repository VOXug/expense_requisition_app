# Expense Requisition App

Custom ERPNext app for managing expense requisitions.

## Features

- Expense Requisition DocType
- Multi-level approval workflow (Submitted -> Manager Approved -> Finance Approved -> Paid)
- Role-based permissions (Employee, Manager, Finance)
- Attachments for receipts
- Integration with Budget Control (future)

## Installation

```bash
bench get-app https://your-git-repo-url/expense_requisition_app.git --branch version-15
bench --site your_site_name install-app expense_requisition_app
```

## License

MIT
