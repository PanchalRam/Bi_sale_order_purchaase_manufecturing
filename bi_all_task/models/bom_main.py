from odoo import api, fields, models, _


class Duplicate_second_Product(models.Model):
    _inherit = 'product.template'

    def copy(self, main_product=None):
        if main_product is None:
            main_product = {}
        copy_product_id = super(Duplicate_second_Product, self).copy()
        product_bom_obj = self.env['mrp.bom'].search([('product_tmpl_id.id', '=', self.id)])
        for bom_main in product_bom_obj:
            bom_main.copy({'product_tmpl_id': copy_product_id.id})
        return copy_product_id
    