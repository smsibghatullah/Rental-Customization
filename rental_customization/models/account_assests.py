from odoo import models, fields,api

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    is_rental_product = fields.Boolean(string="Is Rental Product")
    is_fleet = fields.Boolean(string="Is Fleet")
    fleet_model_id = fields.Many2one('fleet.vehicle.model', string='Fleet Model', required=False)
    

    @api.model_create_multi
    def create(self, vals):

        res = super(AccountAsset, self).create(vals)
        print('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppp') 
        print(res)
        for asset in res:
            if asset.is_rental_product:
                product_template_obj = self.env['product.template']
                product_template_vals = {
                    'name': asset.name,
                    # 'type': 'consu',
                    'rent_ok': True,  
                    'purchase_ok': False, 
                    'sale_ok': False, 
                }
                product_template_obj.create(product_template_vals)

            if asset.is_fleet and asset.fleet_model_id.id:
                fleet_obj = self.env['fleet.vehicle']
                fleet_vals = {
                    'model_id': asset.fleet_model_id.id, 
                }
                fleet_obj.create(fleet_vals)
                
        return res
