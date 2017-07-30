# -*- coding: utf-8 -*-
# © 2016-2017 MIROUNGA <http://mirounga.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    use_hosting = fields.Boolean(
        string='Hosting', help='Hosting account')
    period_invoice = fields.Integer(
        string='Period to invoice', help='Period to invoice in month',
        default=1)
    next_invoice_date = fields.Date(
        string='Next invoice', help='Date for the next invoice date')
    hosting_line_ids = fields.One2many(
        'hosting.analytic.lines', 'contract_id', string='Lines',
        help='Lines to invoice')


class HostingAnalyticLines(models.Model):
    _name = 'hosting.analytic.lines'
    _description = 'Lines to invoice'
    _rec_name = 'product_id'

    contract_id = fields.Many2one(
        'account.analytic.account', string='Contract',
        help='Contract link to this lines')
    product_id = fields.Many2one(
        'product.product', string='Product', help='Product to invoice')
    product_qty = fields.Float(
        string='Quantity', digits_compute=dp.get_precision('Product UoS'),
        help='Quantity to invoice per period')
    product_uom_id = fields.Many2one(
        'product.uom', string='Unit', help='Unit of measure to invoice')
    sequence = fields.Integer(
        string='Sequence', help='Sequence to order lines in invoices')

    @api.onchange('product_id')
    def _onchange_product(self):
        self.product_uom_id = self.product_id.uom_id.id
