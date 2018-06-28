# © 2018 Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{   # pylint: disable=C8101,C8103
    'name': "Integração de pagamentos via CNAB 240",
    'summary': """
        Permite enviar pagamentos a fornecedores via integração bancária
        (CNAB 240) - Mantido por Trustcode""",
    'description': """
        Permite enviar pagamentos a fornecedores via integração bancária
        (CNAB 240) - Mantido por Trustcode""",
    'author': "Trustcode",
    'website': "http://www.trustcode.com.br",
    'category': 'account',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Guilherme Lenon da Silva <guilhermelds@gmail.com>',
        'Marina Domingues <mgd.marinadomingues@gmail.com>'
    ],
    'depends': [
        'br_boleto'
    ],
    'data': [
        'views/br_payment_cnab_views.xml',
        'views/payment_order.xml',
    ],
}