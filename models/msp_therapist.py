from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _


class MspTherapist(models.Model):
    _name = 'msp.therapist'
    _rec_name = 'therapist'
    _description = 'Therapist'

    therapist = fields.Many2one('res.partner',
                                string='Therapist',
                                required=True)
    therapist_image = fields.Binary(string='Photo')
    therapist_id = fields.Char(string='Therapist ID', readonly=True)
    name = fields.Char(string='Therapist ID', default=lambda self: _('New'))
    level = fields.Many2one('therapist.level', string='Level')
    emergency_contact = fields.Many2one('res.partner',
                                        string='Emergency Contact')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'),
                               ('ot', 'Other')],
                              'Gender',
                              required=True)
    dob = fields.Date(string='Date Of Birth', required=True)
    age = fields.Char(string='Age', compute='compute_age')
    visa_info = fields.Char(string='Visa Info', size=64)
    id_proof_number = fields.Char(string='ID Proof Number')
    note = fields.Text(string='Note')
    date = fields.Datetime(string='Date Requested',
                           default=lambda s: fields.Datetime.now(),
                           invisible=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)

    @api.multi
    def compute_age(self):
        for data in self:
            if data.dob:
                dob = fields.Datetime.from_string(data.dob)
                date = fields.Datetime.from_string(data.date)
                delta = relativedelta(date, dob)
            data.age = str(delta.years) + ' years'

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('msp.therapist')
        vals['name'] = sequence or _('New')
        result = super(MspTherapist, self).create(vals)
        return result

    # @api.onchange('therapist')
    # def detail_get(self):
    #     self.phone = self.therapist.phone
    #     self.email = self.therapist.email
