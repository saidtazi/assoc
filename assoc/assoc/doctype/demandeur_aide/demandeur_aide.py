# -*- coding: utf-8 -*-
# Copyright (c) 2020, TAZI Said and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class DemandeurAide(Document):
	def before_save(self):
		self.demandeur_name = self.nom + ' ' + self.prenom
		self.conjoint_name = self.nom_conj + ' ' + self.prenom_conj
