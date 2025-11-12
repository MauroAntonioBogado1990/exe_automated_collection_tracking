from odoo import models, api

class MailTemplate(models.Model):
    _inherit = 'mail.template'

    @api.model
    def generate_email(self, res_ids, fields):
        res = super().generate_email(res_ids, fields)
        for record_id in res_ids:
            partner = self.env['res.partner'].browse(record_id)
            cc_emails = ','.join(
                partner.child_ids.filtered(lambda c: c.is_account_responsible and c.email).mapped('email')
            )
            res[record_id]['email_cc'] = cc_emails
        return res