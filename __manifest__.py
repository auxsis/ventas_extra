# -*- coding: utf-8 -*-
{
    'name': "Ventas extra",

    'summary': """
        Funcionalidad para ventas
    """,

    'description': """
        Funcionalidad para ventas
    """,

    'author': "Rodolfo Borstcheff",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale', 'account'],

    'data': [
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/sale_views.xml',
        'views/account_invoice_views.xml',
        'views/account_views.xml',
    ],
}
