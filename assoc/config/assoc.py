from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Associations"),
			"icon": "octicon octicon-briefcase",
			"items": [
				{
					"type": "doctype",
					"name": "Association",
					"label": _("Association"),
					"description": _("Documents assigned to you and by you."),
					"onboard": 1,
				},
			]
		}
	]
