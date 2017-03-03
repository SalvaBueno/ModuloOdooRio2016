# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

##########################################################################

{
	'name': 'Lista Rio 2016 Salva',
	'version': '1.0',
	'author': 'Salvador Bueno Avila',
	'category': 'Deporte',
	'summary': 'Ejemplo de un modulo de odoo',
    'website': 'salvabuenoavila@gmail.com',
	'description': """
Modulo de Atletas de rio2016 para la clase de Sistemas de Gestion empresarial.
=========================
Esto es un trabajo para entregar.
    """,
	'license': 'AGPL-3',
    'depends': ['sale'],
	'update_xml': [
		'rio2016_view.xml',
	],
	'installable': True,
	'active': False,
}
		