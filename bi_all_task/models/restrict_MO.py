from odoo import api, models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    user_mo = fields.Boolean(string='User Restriction MO')
    all_users = fields.Many2many('res.users', string='Allowed Users')
