from odoo import models

class AccountFollowupLine(models.Model):
    _inherit = 'account_followup.followup.line'

    def _get_followup_mail_template_context(self, partner):
        """Extendemos el contexto del template para incluir CC a responsables"""
        context = super()._get_followup_mail_template_context(partner)

        # Buscar contactos hijos responsables
        cc_emails = ','.join(
            partner.child_ids.filtered(lambda c: c.is_account_responsible and c.email).mapped('email')
        )

        # Agregar al contexto si hay responsables
        if cc_emails:
            context['email_cc'] = cc_emails

        return context