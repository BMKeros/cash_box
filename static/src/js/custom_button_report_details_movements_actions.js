openerp.cash_box = function (instance, local) {
    var QWeb = openerp.web.qweb;
    var _t = instance.web._t;
    var self = this;

    instance.web.ListView.include({
        render_buttons: function (_node) {
            var self = this;
            var add_button = false;
            if (!this.$buttons) { // Ensures that this is only done once
                add_button = true;
            }
            this._super.apply(this, arguments); // Sets this.$buttons
            if (add_button) {
                this.$buttons.find('#bmk_btn_print_report_details_inflow')
                    .click(this.proxy('action_print_details_inflow'));

                this.$buttons.find('#bmk_btn_print_report_details_outflow')
                    .click(this.proxy('action_print_details_outflow'));


                var Users = new openerp.web.Model('res.users');

                Users.call('has_group', ['cash_box.group_cash_box_manager']).done(function (_has_group) {
                    if (_has_group) {
                        self.$buttons.find('#bmk_btn_print_report_details_outflow').removeClass('o_hidden');
                        self.$buttons.find('#bmk_btn_print_report_details_inflow').removeClass('o_hidden');
                    }
                });
            }
        },
        action_print_details_inflow: function () {
            var self = this;
            var model = new instance.web.Model("cash_box.inflow_seat");

            model.call("print_report_details_movements", {context: new instance.web.CompoundContext()}).then(function (result) {
                self.do_action(result);
            });
        },

        action_print_details_outflow: function () {
            var self = this;
            var model = new instance.web.Model("cash_box.outflow_seat");

            model.call("print_report_details_movements", {context: new instance.web.CompoundContext()}).then(function (result) {
                self.do_action(result);
            });
        },

    });
};