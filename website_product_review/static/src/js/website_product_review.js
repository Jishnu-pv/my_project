odoo.define('website_sale_comparison.comparison', function (require) {
events: {
    "click .send": "display_review",
},
display_review: function () {
    console.log('Button Clicked')
}
});