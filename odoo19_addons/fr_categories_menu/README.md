# F&R Categories Menu (Odoo 19)

This addon ports the requested categories dropdown/submenu design into Odoo 19 website assets and templates.

## Install

1. Copy `odoo19_addons/fr_categories_menu` into your Odoo addons path.
2. Update Apps list.
3. Install **F&R Categories Menu**.
4. Open `/categories-preview` to review the layout.

## Technical Notes

- Uses `web.assets_frontend` for SCSS and JS.
- The UI is rendered by the `fr_categories_menu.categories_menu_component` QWeb template.
- Route: `/categories-preview` (public website page).
