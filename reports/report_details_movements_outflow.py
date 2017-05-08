from odoo import api, models

class ReportDetailsMovementsOutflow(models.AbstractModel):
    _name = 'report.cash_box.report_details_movements_outflow'

    @api.model
    def _get_name_month(self, date):
        months = {
            '01': "January",
            '02': "February",
            '03': "March",
            '04': "April",
            '05': "May",
            '06': 'June',
            '07': 'July',
            '08': "August",
            '09': "September",
            '10': "October",
            '11': "November",
            '12': "December",
        }

        date = date.split('-')

        return months.get(date[1], None)

    @api.model
    def render_html(self, docids, data=None):

        report_obj = self.env['report']
        report = report_obj._get_report_from_name('cash_box.report_details_movements_outflow')

        models = self.env['cash_box.outflow_seat'].search([])
        reg = []
        tmp = {}

        for r in models:

            name_month = self._get_name_month(r.created_date)

            if tmp.get(name_month, None) is None:
                tmp[name_month] = {'name':name_month, 'movements_months':[], 'total_amount': 0}

            tmp[name_month]['movements_months'].append(r)

        reg = tmp.values()

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': [],
            'data': reg,
        }

        return report_obj.render('cash_box.report_details_movements_outflow', docargs)