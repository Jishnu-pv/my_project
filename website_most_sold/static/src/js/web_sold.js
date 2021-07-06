odoo.define('website.MostSold', function (require) {
"use strict";

var ajax = require('web.ajax');
var core = require('web.core');
var CrashManager = require('web.CrashManager').CrashManager;
var Dialog = require('web.Dialog');

var _t = core._t;
var QWeb = core.qweb;
//var self = this;
//To get value from the required field.ajax.jsonRpc('/url, 'call', {'test_variable' : test_variable,});

ajax.jsonRpc("/website_most_sold/products", 'call')
//.then(function (data) {
//            if(data){
//                this.$target.empty().append(data);
//            }
//        });

//var def = this._rpc({
//                route: "/website_most_sold/products",
//                params: {
//                    template: template,
//                },
//            })
// return $.when(this._super.apply(this, arguments), def);
});