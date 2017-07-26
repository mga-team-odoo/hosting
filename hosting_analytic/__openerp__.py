# -*- coding: utf-8 -*-
# © 2016-2017 MIROUNGA <http://mirounga.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Analytic account for hosting",
    'version': "8.0.1.0.0",
    'author': "Mirounga, Christophe CHAUVET",
    'license': "AGPL-3",
    'website': "http://www.mirounga.fr",
    'category': "Accounting & Finance",
    'depends': [
        'base',
        'account',
        'analytic',
    ],
    'data': [
        'views/menu.xml',
        'views/analytic.xml',
    ],
    'application': False,
    'installable': True,
    # 'pre_init_hook': 'pre_init_hook',
}
