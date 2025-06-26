{
    'name': 'Test',
    'version': '1.0',
    'category': 'Test',
    'sequence': 15,
    'summary': 'Test Module',
    'website': 'trescloud.com',
    'depends': [
        'account',
    ],
    'data': [
        # security
        'security/delivery_detail_security.xml',
        'security/ir.model.access.csv',
        # data
        #'data/mrp_rework.xml',
        # views
        'views/account_move_views.xml',
        'views/delivery_detail_views.xml',
        # reports
        'reports/report_invoice_templates.xml',
        # wizard
        #'wizard/create_rework_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
