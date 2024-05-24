# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import getseries


class Airplane(WebsiteGenerator):
	def autoname(self):
		prefix = "{}-".format(self.airline)
		self.name = prefix + getseries(prefix,1).zfill(5)

