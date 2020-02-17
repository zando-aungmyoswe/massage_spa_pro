# -*- coding: utf-8 -*-
{
    'name':
    "Massage Spa Pro",
    'summary':
    """
        Massage Spa Pro For your businness improveent""",
    'description':
    """
        Massage Spa Pro
    """,
    'author':
    "Light Soft",
    'website':
    "http://www.lightsoft.com",
    'category':
    'Uncategorized',
    'version':
    '0.1',
    'depends': ['base', 'product'],
    'data': [
        'security/msp_users.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/therapist_level.xml',
        'views/res_partner.xml',
        'views/msp_therapist_view.xml',
        'views/msp_commission_type.xml',
        'views/msp_room.xml',
        'views/product_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':
    True,
    'application':
    True,
}
