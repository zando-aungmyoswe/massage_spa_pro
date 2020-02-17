# -*- coding: utf-8 -*-
from odoo import http

# class MassageSpaPro(http.Controller):
#     @http.route('/massage_spa_pro/massage_spa_pro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/massage_spa_pro/massage_spa_pro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('massage_spa_pro.listing', {
#             'root': '/massage_spa_pro/massage_spa_pro',
#             'objects': http.request.env['massage_spa_pro.massage_spa_pro'].search([]),
#         })

#     @http.route('/massage_spa_pro/massage_spa_pro/objects/<model("massage_spa_pro.massage_spa_pro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('massage_spa_pro.object', {
#             'object': obj
#         })