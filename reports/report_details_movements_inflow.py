from odoo import api, models, _

class ReportDetailsMovementsInflow(models.AbstractModel):
    _name = 'report.cash_box.report_details_movements_inflow'

    @api.model
    def _get_name_month(self, date):
        months = {
            '01': _("January"),
            '02': _("February"),
            '03': _("March"),
            '04': _("April"),
            '05': _("May"),
            '06': _('June'),
            '07': _('July'),
            '08': _("August"),
            '09': _("September"),
            '10': _("October"),
            '11': _("November"),
            '12': _("December"),
        }

        date = date.split('-')

        return months.get(date[1], None)

    @api.model
    def render_html(self, docids, data=None):

        report_obj = self.env['report']
        report = report_obj._get_report_from_name('cash_box.report_details_movements_inflow')

        models = self.env['cash_box.inflow_seat'].search([])
        tmp = {}

        for r in models:

            name_month = self._get_name_month(r.created_date)

            if tmp.get(name_month, None) is None:
                tmp[name_month] = {'name':name_month, 'movements_months':[], 'total_amount': 0}

            tmp[name_month]['movements_months'].append(r)
            tmp[name_month]['total_amount'] += r.amount


        reg = tmp.values()

        currency = self.env['res.company']._company_default_get('cash_box').currency_id

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': [],
            'data': reg,
            'currency_company': currency
        }

        return report_obj.render('cash_box.report_details_movements_inflow', docargs)