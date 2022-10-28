
const { expect } = require("chai");
const sinon = require('sinon')
const Utils = require("./utils");
const sendPaymentRequestToApi = require('./4-payment');

describe("compare two add functions", function() {
  it("checks equality", function() {
    const stubbedFunc = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spiedStub = sinon.spy(stubbedFunc);
    stubbedFunc(100, 20);
    expect(spiedStub.calledWith(100, 20)).to.be.false;
    spiedFunc.restore();
  })});
