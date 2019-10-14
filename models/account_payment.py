# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.multi
    @api.onchange('payment_date')
    def change_payment_date(self):
        if self.user_has_groups('sales_team.group_sale_salesman'):
            return {'domain': {'journal_id': ['&',('permitir_pagos','=',True),('type', 'in', ('bank', 'cash'))]}}
