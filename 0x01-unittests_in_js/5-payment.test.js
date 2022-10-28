
const { expect } = require("chai");
const sinon = require('sinon')
const Utils = require("./utils");
const sendPaymentRequestToApi = require('./5-payment');

describe("compare two add functions", function() {
  it("checks equality", function() {
    let spy = sinon.spy(sendPaymentRequestToApi)
    beforeEach( () => {
      sendPaymentRequestToApi(100, 20);
    })
    afterEach( () => {
      spy.restore();
    })
    expect(sendPaymentRequestToApi.calledWith(100, 20)).to.be.true;
    expect(sendPaymentRequestToApi.calledWith(10, 2)).to.equal(20);
  })});
