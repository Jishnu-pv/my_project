odoo.define('point_of_sale.PaymentMethodCreditButton', function(require) {
    'use strict';
    var models = require('point_of_sale.models');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    models.load_fields('res.partner','due_limit');
    models.load_fields('res.partner','credit');
    models.load_fields('res.partner','debit');
    var PaymentScreen = require('point_of_sale.PaymentScreen');



   const MyPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
        addNewPaymentLine({ detail: paymentMethod}){
        console.log("here get client",this.currentOrder.get_due())

        console.log("check",paymentMethod.name);

        if(paymentMethod.name == 'Credit' && !this.currentOrder.get_client()){
        this.showPopup('ConfirmPopup',{
        title: this.env._t('Error'),
        body: this.env._t('Select Customer')
        });
        }
        else if(!this.currentOrder.get_client().due_limit){
        this.showPopup('ConfirmPopup',{
            title: this.env._t('Eroor'),
            body: this.env._t('Customer dont have any Credit!!!')
           });
        }

        else if(paymentMethod.name == 'Credit' &&
        this.currentOrder.get_client().due_limit <
        (this.currentOrder.get_due()+this.currentOrder.get_client().credit)){
            this.showPopup('ConfirmPopup',{
            title: this.env._t('Eroor'),
            body: this.env._t('Amount Greater than Due Limit')
           });
        }
        else{
                this.currentOrder.get_client().due_Limit = this.currentOrder.get_client().due_limit - this.currentOrder.get_total_with_tax()
                console.log("balance",this.currentOrder.get_client().due_Limit);
                const order = this.env.pos.get_order();
                const res = super.addNewPaymentLine(...arguments);
                if (res && paymentMethod.pos_mercury_config_id) {
                    order.selected_paymentline.mercury_swipe_pending = true;
                    order.trigger('change', order);
                    this.render();
                }
                return this.currentOrder.get_client().due_Limit
        }



        }


    }

    console.log("hahahahheee")
    Registries.Component.extend(PaymentScreen, MyPaymentScreen);

    });

//    class PaymentMethodCreditButton extends PosComponent {
//    constructor() {
//                super(...arguments);
//                useListener('click', this.onClick);
//            }
////   $('.payment-name').click(function(){
////     alert("hello");
////   })
//      onClick(){
//      console.log("hereree")
//
//
//      }
//
//
//
//    }
//
//    console.log("hai hello aaa")
//
//
//
//    return PaymentMethodCreditButton;
//});
