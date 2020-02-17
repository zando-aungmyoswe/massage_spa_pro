from odoo import models, fields


class TherapistLevel(models.Model):
    _name = 'therapist.level'
    _description = 'Therapist Level'

    name = fields.Char(string='Name', required=True)
    commissiontype_id = fields.Many2one('msp.commissiontype',
                                        'Commission Type')
    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'Name must be unique!')]
