const utils = require('./utils')


function sendPaymentRequestToApi(totalAmount, totalShipping) {
total = utils.calculateNumber('SUM', totalAmount, totalShipping);
console.log(`The total is: ${total}`)
}

module.exports = sendPaymentRequestToApi
