const chai = require("chai");
const expect = chai.expect;
const sinon = reqire('sinon')
const Utils = require("./utils");
const totalC = require('./3-payment');

describe("compare two add functions", function() {
  it("checks equality", function() {
    const spiedFunc = sinon.spy(Utils, calculateNumber);
    totalC(100, 20);
    expect(spiedFunc.calledWith('SUM', 100, 20)).to.be.true;
    spiedFunc.restore();
  })});
