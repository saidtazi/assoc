from frappe import _

def get_data():
	return {
		'fieldname':'demandeur_aide',
		'transactions': [
			{
				'label':_('Opérations'),
				'items':['Distribution Aide']
			}
		]
	}
