from odoo import models, fields,api

class Purchase_order(models.Model):
    _inherit='purchase.order'
    purchase_order = fields.Boolean(string='purchase order')
    