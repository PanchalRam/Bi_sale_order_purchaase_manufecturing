from odoo import fields, models, api, _


class ProductAvailableQuantityWizard(models.TransientModel):
    _name = "product.available.wizard"
    _description = "Product Available Quantity Wizard"

    stocck_warehouse_ids = fields.Many2many('stock.quant')
    product_main_id = fields.Many2one('product.product', string='Product Name')

    def default_get(self, fields):
        product_list = []
        active_id = self._context.get('active_ids')
        print("active_id",active_id)
        purchase_order_obj = self.env['purchase.order']
        print("purchase_order_obj",purchase_order_obj)
        purchase_line_ids = purchase_order_obj.order_line.browse(active_id)
        print("purchase_line_ids",purchase_line_ids)
        stock_quant_obj = self.env['stock.quant']
        print('stock_quant_obj',stock_quant_obj)
        stock_quant_search_ids = stock_quant_obj.search([('product_id', '=', purchase_line_ids.product_id.id),
                            ('location_id.usage', '=', 'internal')])                         
        for record in stock_quant_search_ids:
            product_list.append(record.id)

        return {
            'product_main_id': purchase_line_ids.product_id.id,
            'stocck_warehouse_ids': [(6, 0, product_list)]
        }
