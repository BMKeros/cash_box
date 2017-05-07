from odoo import api, models

class ReportDetailsMovementsInflow(models.AbstractModel):
    _name = 'report.cash_box.report_details_movements_inflow'

    @api.model
    def render_html(self, docids, data=None):

        report_obj = self.env['report']
        report = report_obj._get_report_from_name('cash_box.report_details_movements_inflow')

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': [],
            'data': self.env['cash_box.inflow_seat'].search([]),
        }

        return report_obj.render('cash_box.report_details_movements_inflow', docargs)
