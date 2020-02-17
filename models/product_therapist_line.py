# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTherapistLine(models.Model):
    _name = 'product.therapist.line'

    product_tmpl_id = fields.Many2one("product.template", "Product Template")
    name = fields.Many2one("msp.therapist", "Name")
    price = fields.Float("price")
