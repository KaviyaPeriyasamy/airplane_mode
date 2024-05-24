// Copyright (c) 2024, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    validate: function (frm) {
		frappe.call({
            method: "airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.validate_capacity",
            args: {
                flight: frm.doc.flight
            },
        });
	},
	refresh(frm) {
        frm.add_custom_button(
            __("Assign Seat"),
            function () {
                var d = new frappe.ui.Dialog({
                    title: __("Select"),
                    fields: [
                        {
                            label: "Seat Number",
                            fieldname: "seat_number",
                            fieldtype: "Data",
                            reqd: 1
                        },
                    ],
                    primary_action: function () {
                        var data = d.get_values();
                        frm.set_value("seat", data.seat_number);
                        frm.save();
                        d.hide();
                    },
                    primary_action_label: __("Assign"),
                });
                d.show();
            },
            __("Actions")
        );
	},
});
