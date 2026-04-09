from odoo import http
from odoo.http import request


class FrCategoriesMenuController(http.Controller):
    @http.route("/categories-preview", type="http", auth="public", website=True)
    def categories_preview(self, **kwargs):
        return request.render("fr_categories_menu.categories_preview_page")
