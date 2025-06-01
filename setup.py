from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in expense_requisition_app/__init__.py
from expense_requisition_app import __version__ as version

setup(
	name="expense_requisition_app",
	version=version,
	description="Custom ERPNext app for managing expense requisitions.",
	author="Manus AI Agent",
	author_email="support@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
