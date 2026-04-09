{
    "name": "F&R Categories Menu",
    "version": "19.0.1.0.0",
    "summary": "Website categories dropdown and submenu design for Odoo 19",
    "category": "Website",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/categories_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "fr_categories_menu/static/src/scss/categories_menu.scss",
            "fr_categories_menu/static/src/js/categories_menu.js",
        ],
    },
    "installable": True,
    "application": False,
}
