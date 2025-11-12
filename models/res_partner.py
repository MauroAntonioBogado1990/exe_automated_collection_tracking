# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_account_responsible = fields.Boolean(string="Responsable de cuenta corriente")