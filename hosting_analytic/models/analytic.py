# -*- coding: utf-8 -*-
# © 2016-2017 MIROUNGA <http://mirounga.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    use_hosting = fields.Boolean(
        string='Hosting', help='Hosting account')
    period_invoice = fields.Integer(
        string='Period to invoice', help='Period to invoice in month',
        default=1)
    next_invoice_date = fields.Date(
        string='Next invoice', help='Date for the next invoice date')
