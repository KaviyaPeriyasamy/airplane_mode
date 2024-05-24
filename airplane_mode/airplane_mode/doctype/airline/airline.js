// Copyright (c) 2024, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        const website = frm.doc.website;
        if (website){        
            frm.add_web_link(website, __("Visit Website"));
        }
	},
});
