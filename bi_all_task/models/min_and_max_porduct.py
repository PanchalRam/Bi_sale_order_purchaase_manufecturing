from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class Product_Product(models.Model):
    _inherit = 'product.product'

    min_amount = fields.Float(string="Max Amount")
    max_amount = fields.Float(string="Min Amount")

class Sale_Order_Line(models.Model):
    _inherit = 'sale.order.line'

    minamount = fields.Float(string="Max Amount")
    maxamount = fields.Float(string="Min Amount")

    @api.onchange('product_id')
    def onchange_product(self):
        for rec in self:
            rec.minamount = rec.product_id.min_amount
            rec.maxamount = rec.product_id.max_amount

class Sale_Order(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        print(":::::::Enter:::::::::::")
        for rec in self:
            if rec.order_line.price_unit <= rec.order_line.maxamount or rec.order_line.price_unit >= rec.order_line.minamount: 
                if not self.env.user.has_group('sale_min_max_module.sale_min_max_bool'):
                    print("::::::::::::::::::in the function::::::::::::::::::")
                    raise ValidationError(_('Price Unit must be within minprice & max price'))
            return  super(Sale_Order,self).action_confirm()
    