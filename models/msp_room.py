from odoo import models, api, fields, _


class MSPRoom(models.Model):
    _name = 'msp.room'
    _description = 'Room'

    name = fields.Char(string='Room ID')
    room_id = fields.Char(string='Room ID',
                          readonly=True,
                          default=lambda self: _('New'))
    capacity = fields.Integer(string='Capicity')
    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'Name must be unique!')]

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('msp.room')
        vals['room_id'] = sequence or _('New')
        result = super(MSPRoom, self).create(vals)
        return result
