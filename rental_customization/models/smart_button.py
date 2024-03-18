from odoo import models, api,fields
from odoo.exceptions import UserError

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    fleet_vehicle_count = fields.Integer(string="Fleet Vehicle Count", compute='_compute_fleet_vehicle_count')
    rental_count = fields.Integer(string="Rental Count", compute='_compute_rental_count')

    @api.depends('fleet_model_id')
    def _compute_fleet_vehicle_count(self):
        for asset in self:
            if asset.fleet_model_id:
                asset.fleet_vehicle_count = self.env['fleet.vehicle'].search_count([('account_asset_id', '=', asset.id)])
            else:
                asset.fleet_vehicle_count = 0

    def action_open_fleet(self):
        if not self.fleet_model_id:
            raise UserError("No fleet model associated with this asset.")
        fleet_vehicles = self.env['fleet.vehicle'].search([('account_asset_id', '=', self.id)])
        if not fleet_vehicles:
            raise UserError("No fleet vehicles associated with the fleet model of this asset.")

        form_id = self.env.ref("fleet.fleet_vehicle_view_form").id

        return {
            "name": fleet_vehicles[0].name,
            "view_mode": "form",
            "res_model": "fleet.vehicle",
            "res_id": fleet_vehicles[0].id,
            "type": "ir.actions.act_window",
            "target": "current",
        }
    

    def _compute_rental_count(self):
        for asset in self:
            if asset.is_rental_product:
                asset.rental_count = self.env['product.template'].search_count([('account_asset_id', '=', asset.id)])
            else:
                asset.rental_count = 0


    def action_open_rental(self):
        if not self.is_rental_product:
            raise UserError("This asset is not associated with any rental product.")

        rental_products = self.env['product.template'].search([('account_asset_id', '=', self.id)])
        if not rental_products:
            raise UserError("No rental products associated with this asset.")

        form_id = self.env.ref("product.product_template_form_view").id
        return {
            "name": rental_products.name,
            "view_mode": "form",
            "res_model": "product.template",
            "res_id": rental_products.id,
            "type": "ir.actions.act_window",
            "target": "current",
        }
