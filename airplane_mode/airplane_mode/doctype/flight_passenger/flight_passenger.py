# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.full_name = f"{self.first_name}"
		if self.last_name:
			self.full_name += f" {self.last_name}"
