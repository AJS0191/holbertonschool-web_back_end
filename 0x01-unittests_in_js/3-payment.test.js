
const { expect } = require("chai");
const sinon = require('sinon')
const Utils = require("./utils");
const sendPaymentRequestToApi = require('./3-payment');

describe("compare two add functions", function() {
  it("checks equality", function() {
    const spiedFunc = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spiedFunc.calledWith('SUM', 100, 20)).to.equal(120);
    spiedFunc.restore();
  })});
