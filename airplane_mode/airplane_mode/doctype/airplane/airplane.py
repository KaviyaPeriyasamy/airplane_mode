# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries


class Airplane(Document):
	def autoname(self):
		prefix = "{}-".format(self.airline)
		self.name = prefix + getseries(prefix,1).zfill(5)

