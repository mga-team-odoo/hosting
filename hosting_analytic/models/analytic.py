# -*- coding: utf-8 -*-
# © 2016-2017 MIROUNGA <http://mirounga.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields

class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    use_hosting = fields.Boolean(
        string='Hosting', help='Hosting account')

