# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    permitir_pagos = fields.Boolean('Permitir ver en pagos')
