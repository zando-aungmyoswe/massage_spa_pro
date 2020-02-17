from odoo import models, fields, api, _


class MSPCommissionTypeSession(models.Model):
    _name = 'msp.commissiontypesession'
    _description = 'Commission Type Session'

    commissiontype_id = fields.Many2one('msp.commissiontype',
                                        'Commission Type')
    from_session = fields.Integer(string='From')
    to_session = fields.Integer(string='To')
    quota = fields.Float(string='Quota')
