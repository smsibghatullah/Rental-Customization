from odoo import fields, models

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    account_asset_id = fields.Many2one('account.asset', string='Asset Account')
