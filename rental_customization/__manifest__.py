{
    'name': 'rental_customization',
    'version': '1.0',
    'summary': 'rental_customization',
    'sequence': 10,
    'description': """rental_customization""",
    'category': 'Accounting',
    'depends': ['base', 'account_asset','product'],
    'data': [
        'views/account_asset_views.xml',
        'views/product_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
