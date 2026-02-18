{
    'name': 'Controle de Combustível Machado',
    'version': '1.0',
    'summary': 'Gestão de abastecimento e tanques de combustível',
    'description': 'Módulo para controle de estoque de tanques (6000L) e registro de abastecimentos de frota.',
    'author': 'Robson', #
    'category': 'Operations',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/tanque_view.xml',
        'views/abastecimento_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3', # Recomendado para Odoo Community
}