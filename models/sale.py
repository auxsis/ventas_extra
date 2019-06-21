# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        for line in self.order_line:
            if line.discount > self.env.user.limite_descuento:
                raise UserError('El descuento máximo permitido para este usuario es: ' + str(self.env.user.limite_descuento) + '%')
            if line.price_unit < line.product_id.standard_price and not self.env.user.ventas_menor_costo:
                raise UserError('El precio ingresado está por abajo del costo y no es permitido para este usuario.')

        super(SaleOrder, self).action_confirm()
        return True

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit_rel = fields.Float(related='price_unit', string="Precio de Unidad", readonly=True)
