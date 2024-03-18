from odoo import models, fields,api
from odoo.exceptions import UserError

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    is_rental_product = fields.Boolean(string="Is Rental Product")
    is_fleet = fields.Boolean(string="Is Fleet")
    fleet_model_id = fields.Many2one('fleet.vehicle.model', string='Fleet Model', required=False)
    
    

    @api.onchange('model_id')
    def _onchange_model_id(self):
        if self.model_id and self.state != 'model':
            self.is_fleet = self.model_id.is_fleet
            self.is_rental_product = self.model_id.is_rental_product
            self.account_depreciation_expense_id = self.model_id.account_depreciation_expense_id
            self.account_depreciation_id = self.model_id.account_depreciation_id
            self.account_asset_id = self.model_id.account_asset_id

          

    @api.model_create_multi
    def create(self, vals):
        res = super(AccountAsset, self).create(vals)
        for asset in res:
             if asset.state != 'model':
                    if asset.state != 'model' and asset.model_id and not asset.fleet_model_id:
                        raise UserError("For this Asset Model. please select Fleet Model too")
                    if asset.state != 'model' and asset.is_rental_product:
                        product_template_obj = self.env['product.template']
                        print(asset.id,'ggggggggggggggggggggg',asset.name)
                        product_template_vals = {
                            'name': asset.name,
                            'account_asset_id':asset.id,
                            'rent_ok': True,
                            'purchase_ok': False,
                            'sale_ok': False,
                        }
                        product_template_obj.create(product_template_vals)
                    if asset.is_fleet and asset.fleet_model_id:
                        fleet_obj = self.env['fleet.vehicle']
                        fleet_vals = {
                            'model_id': asset.fleet_model_id.id,
                            'account_asset_id': asset.id
                        }
                        fleet_obj.create(fleet_vals)
        return res