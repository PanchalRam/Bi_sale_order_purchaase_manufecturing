from odoo import api, models, fields
from odoo.exceptions import ValidationError,UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    user_mo = fields.Boolean(string='User Restriction MO')
    all_users_ids = fields.Many2many('res.users', string='Users',domain=[('share', '=', False)])
   
    @api.model
    def search(self, vals, offset=0, limit=None, order=None, count=False):
        current_user = self._context.get('uid') 
        user = self.env['mrp.production'].browse(current_user)

        vals += [('all_users_ids', '!=', user.id)]

        return super(MrpProduction, self).search(vals, offset=offset, limit=limit, order=order, count=count)
