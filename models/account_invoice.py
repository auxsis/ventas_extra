# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def action_invoice_open(self):
        for line in self.invoice_line_ids:
            if line.discount > self.env.user.limite_descuento:
                raise UserError('El descuento máximo permitido para este usuario es: ' + str(self.env.user.limite_descuento) + '%')

        res = super(AccountInvoice, self).action_invoice_open()
        return res

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    price_unit_rel = fields.Float(related='price_unit', string="Precio de Unidad", readonly=True)
