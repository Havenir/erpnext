from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'stock_entry',
		'non_standard_fieldnames': {
			'Journal Entry': 'ref_name',
		},
		'internal_ref_type_links': {
			'Purchase Order': ['stock_entry_ref', 'ref_name'],
			'Purchase Invoice': ['stock_entry_ref', 'ref_name'],
		},
		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Journal Entry']
			},
			{
				'label': _('References'),
				'items': ['Purchase Order', 'Purchase Invoice']
			}
		]
	}
