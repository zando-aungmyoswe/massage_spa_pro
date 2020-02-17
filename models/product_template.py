from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    therapist_line = fields.One2many("product.therapist.line",
                                     "product_tmpl_id", "Therapist Line")
