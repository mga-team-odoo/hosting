# -*- coding: utf-8 -*-
# © 2016-2017 MIROUNGA <http://mirounga.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp.tests.common import TransactionCase


class TestCreateInvoice(TransactionCase):
    """
    Create an invoice base on lines on contract
    """
    def setUp(self):
        super(TestCreateInvoice, self).setUp()
        cr, uid = self.cr, self.uid
