# Copyright 2018 Artyom Losev
# Copyright 2018 Dinar Gabbasov <https://it-projects.info/team/GabbasovDinar>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """POS: Pay SO & Invoices""",
    "summary": """Handle the payment process for Sale Orders/Invoices over Point of Sale""",
    "category": "Point of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/pos-invoice-pay?version=11.0",
    "images": ["images/pos_invoice_pay_main.png"],
    "version": "11.0.1.2.3",
    "application": False,
    "author": "IT-Projects LLC, Artyom Losev",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/ArtyomLosev",
    "license": "Other OSI approved licence",  # MIT
    "price": 89.00,
    "currency": "EUR",
    "depends": ["base_automation", "sale_management", "pos_longpolling"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data.xml",
        "actions/base_action_rules.xml",
        "report/report.xml",
        "view.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
    "demo_title": "Pay Sale Orders & Invoices over POS",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "pos-invoice-pay",
    "demo_summary": "Handle the payment process for Sale Orders/Invoices over Point of Sale",
    "demo_images": ["images/pos_invoice_pay_main.png"],
}
