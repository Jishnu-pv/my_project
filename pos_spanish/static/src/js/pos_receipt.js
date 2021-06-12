odoo.define('point_of_sale.PosName', function(require) {
    'use strict';
    var models = require('point_of_sale.models');
    models.load_fields('product.product','spanish_name');
    var _super_orderline = models.Orderline.prototype;

    models.Orderline = models.Orderline.extend({
        export_for_printing: function() {
            var line = _super_orderline.export_for_printing.apply(this,arguments);
            line.spanish_name = this.get_product().spanish_name;
            return line;
            console.log("hao",line)

    },
});
console.log("hao")


    });


//    odoo.define('point_of_sale.PosName', function(require) {
//    'use strict';
//    var models = require('point_of_sale.models');
//    models.load_fields('product.template','spanish_name');
//
//    class PosName extends ProductItem {
//        get user() {
//                return models.spanish_name;
//            }
//        }
//
//    });




