from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    account_asset_id = fields.Many2one('account.asset', string='Asset', nullable=True)
