# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'PDF Report Preview',
    'author': 'VnSoft',
    'maintainer': 'Odoog',
    'support': 'vnsoft.he@gmail.com',
    'website': 'https://www.odoog.com',
    'summary': "PDF Report Preview",
    'description': """Modify the Odoo report printing method to support direct preview of PDF data stream, without the need to perform a download action.""",
    'version': '17.0.1.0.0',
    'sequence': 99,
    'category': 'tools',
    'depends': ['web'],
    #"excludes": ["web_enterprise"],
    'qweb': [],
    'assets': {
        'web.assets_backend': [
            'og_qweb_pdf_preview/static/src/js/pdf_preview.js',
        ],
    },
    'images': ["static/description/screen.png"],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
