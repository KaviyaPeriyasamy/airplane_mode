# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ShopContract(Document):
	def on_submit(self):
		self.rent_amount = frappe.db.get_singles_value("Airport Shop Settings", "default_rent_amount_for_shop")
