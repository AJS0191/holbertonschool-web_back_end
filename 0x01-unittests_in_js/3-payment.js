const utils = require('./utils')
const calc = utils.calculateNumber

function sendPaymentRequestToApi(totalAmount, totalShipping) {
total = calc('SUM', totalAmount, totalShipping);
console.log(`The total is: ${total}`)
}

module.exports = sendPaymentRequestToApi
