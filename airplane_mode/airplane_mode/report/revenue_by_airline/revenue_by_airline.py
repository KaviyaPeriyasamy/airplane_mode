# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe import  _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data()
	chart = get_chart_data(data)
	report_summary = get_report_summary(data)
	return columns, data, None, chart, report_summary

def get_columns():
	columns = [
		{
			"fieldname": "airline",
			"label": _("Airline"),
			"fieldtype": "Link",
			"options": "Airline",
			"width": 300,
		},
		{
			"fieldname": "revenue",
			"label": _("Revenue"),
			"fieldtype": "Currency",
			"width": 300,
		}
	]
	return columns

def get_data():
	final_data = []
	airlines = frappe.get_list('Airline')
	tickets = frappe.get_list('Airplane Ticket',['name','airline','total_amount'])
	for airline in airlines:
		total_amount = 0
		for ticket in tickets:
			if ticket['airline'] == airline.name:
				if ticket['total_amount']:
					total_amount += ticket['total_amount']
		final_data.append({
			'airline': airline.name,
			'revenue': total_amount
		})
	return final_data

def get_chart_data(data):
	if not data:
		return None

	revenue = []
	labels = []

	for entry in data:
		revenue.append(entry['revenue'])
		labels.append(_(entry['airline']))

	chart = {
		"data": {
			"labels": labels,
			"datasets": [{"name": _("Airlines"), "values": revenue}],
		},
		"type": "donut",
		"colors": ["green", "red", "blue"],
	}

	return chart

def get_report_summary(data):
	if not data:
		return None

	total_revenue = sum([entry['revenue'] for entry in data])

	return [
		{
			"value": total_revenue,
			"label": _("Total Revenue"),
			"indicator": "Green" if total_revenue > 0 else "Red",
			"datatype": "Currency",
		}
	]