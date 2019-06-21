# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Users(models.Model):
    _inherit = 'res.users'

    limite_descuento = fields.Float(string='Límite')
    ventas_menor_costo = fields.Boolean(string='Permitir vender a menos que el costo')
