# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _

class rio2016_modelo(osv.osv):
	_name = 'rio2016.modelo'
	_description = 'Formulario atletas'
	_columns = {
		'nombre' : fields.char('Nombre' , size=256, required = True, help ='Este es el nombre'),
        'pais' : fields.char('Pais' , size=256, required = True, help ='Este es el pais'),
		'oro' : fields.integer('Oro', required= True),
		'plata' : fields.integer('Plata', required=True),
		'active': fields.boolean('Activo'),
	}
	_defaults = {
		'active' : 'true',
	}
rio2016_modelo()