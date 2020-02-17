from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_therapist = fields.Boolean(string='Is Therapist')
    is_member = fields.Boolean(string='Is Member')
