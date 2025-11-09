# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (c) 2021 CDS Solutions SRL. (https://cdsegypt.com)
#    Maintainer: Eng.Ramadan Khalil (<ramadan.khalil@cdsegypt.com>)
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "Product Price Display",
    'summary': """
        Adds an option in POS Settings to display each product’s price below the product card in the POS interface.
    """,
    'description': """
        This module introduces a simple but powerful enhancement to the Odoo Point of Sale interface by allowing POS users to display product prices directly under product cards.
        Key Features
        Adds a new setting in Point of Sale → Configuration to enable or disable product price display.
        When activated, the POS UI will show the product’s price below each product card.
        Fully integrated with Odoo’s POS price computation, including:
        Pricelists
        Taxes
        Discounts
        Multi-currency (if applicable)
        Lightweight and compatible with all POS themes.
        No impact on POS performance.
        Benefits
        Provides clearer pricing visibility to POS cashiers.
        Reduces mistakes when selecting products with similar images.
        Enhances user experience by showing essential information directly in the product grid.
    """,
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