from odoo import models, fields, api, _


class MSPCommissionType(models.Model):
    _name = 'msp.commissiontype'
    _description = 'Commission Type'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    calculation_method = fields.Selection([('percentage', 'Percentage'),
                                           ('session', 'Session')],
                                          'Calculation Method',
                                          required=True,
                                          default="percentage")
    rate = fields.Float(string='Rate')
    commissiontype_session = fields.One2many('msp.commissiontypesession',
                                             'commissiontype_id',
                                             'Commission Type Session')

    @api.multi
    def toggle_active(self):
        for ct in self:
            if not ct.active:
                ct.active = self.active
        super(MSPCommissionType, self).toggle_active()