{
    'name': 'All task model',
    'category': 'Manufacturing',
    'version': '16.0.0.0',
    "website":"nsjndn",
    "summary":"PRACTISE",
    "author":"me",
    "depends":['sale', 'sale_management', 'stock', 'mrp','product',"crm","account","purchase","sale_management","stock",],
    "installable":True,
    "appplication":True,
    "license":"LGPL-3",
    "auto_install":False,
    "data": [
        'security/ir.model.access.csv',
        'security/security_purchase.xml',
        'security/security_of_MO.xml',
        'security/record_for_saleord.xml',
        'wizard/product_avilabe_wizard.xml',
        'views/purchase_order_views.xml',
        'views/sale_main_server.xml',
        'views/MO_manufecturing.xml',
        'views/min_and_max.xml',
        'wizard/sale_main_wizard.xml'
    ]
}    