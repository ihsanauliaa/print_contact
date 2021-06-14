from odoo import api,fields,models
from odoo.exceptions import Warning,ValidationError,UserError


class extend_contact(models.Model):
    _inherit='res.partner'
    
    @api.multi
    def print_page(self):
        return self.env.ref('print_contact.action_report_page').report_action(self)

    