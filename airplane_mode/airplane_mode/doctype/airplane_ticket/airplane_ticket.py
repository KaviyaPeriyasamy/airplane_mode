# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
	def before_insert(self):
		airplane = frappe.db.get_value('Airplane Flight', self.flight, 'airplane')
		capacity = frappe.db.get_value('Airplane', airplane, 'capacity')
		ticket_count = frappe.db.count(
			"Airplane Ticket",
			{"flight": self.flight},
		)
		if ticket_count > capacity:
			# raise frappe.ValidationError(_("Airplane Capacity is Full"))
			frappe.throw(_("Airplane Capacity is Full"))
		# validate_capacity(self.flight)
	# 	import random
	# 	import string
	# 	self.seat = f'{random.randint(1,99)}' + ''.join(random.choices(string.ascii_uppercase,k=1))
	
	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("You are not allowed to submit this document as status is inappropriate")
	
	def before_save(self):
		final_addons = []
		addon_items = set()
		addons_total = 0

		if self.add_ons:
			for row in self.add_ons:
				if row.item not in addon_items:
					addon_items.add(row.item)
					final_addons.append(row)
					addons_total=addons_total + row.amount
					
			self.set('add_ons',final_addons)
			self.set('total_amount', self.flight_price + addons_total)

# @frappe.whitelist()
# def validate_capacity(flight):
# 	airplane = frappe.db.get_value('Airplane Flight', flight, 'airplane')
# 	capacity = frappe.db.get_value('Airplane', airplane, 'capacity')
# 	ticket_count = frappe.db.count(
# 		"Airplane Ticket",
# 		{"flight": flight},
# 	)
# 	if ticket_count > capacity:
# 		frappe.throw(title='Error',
#     	msg='Airplane Capacity is Full'
# 		)