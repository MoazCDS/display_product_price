# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (c) 2021 CDS Solutions SRL. (https://cdsegypt.com)
#    Maintainer: Eng.Ramadan Khalil (<ramadan.khalil@cdsegypt.com>)
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "Product Price Display",
    'summary': """""",
    'description': """""",
    'author': "CDS Solutions SRL",
    'website': "https://www.cdsegypt.com",
    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
        "Moaz Elbahr <info@cds-solutions.co>",
    ],
    'category': 'Point_of_sale',
    'version': '0.1',
    'depends': ['point_of_sale'],
    'data': [
        "views/pos_config_view.xml"
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'cds_product_price_display/static/src/**/*',
        ],
    },
    'images': ['static/description/banner.gif'],
    'license': 'OPL-1',
    "pre_init_hook": None,
    "post_init_hook": None,
}