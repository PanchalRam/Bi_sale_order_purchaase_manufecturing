from odoo import api, fields, models, _


class Sale_product_Wizard(models.TransientModel):
    _name = "sale.product.wizard"
    _description = "Sale_purchase_Wizard"

    res_user_id = fields.Many2one('res.partner', 'Customer Name',
                                  index=True,
                                  required=True,)
    product_names=fields.Char(readonly=True)                                  
    all_names_id = fields.Many2many(
        'product.product',
        default=lambda self: self._get_default_product())

    def action_confirm(self):
        self.ensure_one()
        order_line_ids = []
        current_model = self.env.context.get('active_model')
        active_id = self.env[current_model].browse(
            self.env.context.get('active_ids'))
        for i in self:
            for rec in active_id:
                order_line_ids.append((0, 0, {
                    'product_id': rec.id,
                }))
            vals = ({
                'partner_id': self.res_user_id.id,
                'order_line': order_line_ids
            })
        create_sale_order = self.env['sale.order'].create(vals)
        action_new_sale_order = {
            'name': _('Sale Order'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'view_id': False,
            'views': [(self.env.ref('sale.view_order_form').id, 'form')],
            'res_id': create_sale_order.id,
        }
        return action_new_sale_order

    @api.onchange('all_names_id')
    def _onchange_all_names_id(self):
        if self.all_names_id:
            product_names = ','.join(self.all_names_id.mapped('name'))
            self.product_names = product_names

    def _get_default_product(self):
        current_model = self.env.context.get('active_model')
        if current_model == 'product.product':
            active_ids = self.env.context.get('active_ids', [])
            products = self.env['product.product'].browse(active_ids)
            product_names = ', '.join(products.mapped('name'))
            self.product_names = product_names
            return [(6, 0, products.ids)] 
        return False