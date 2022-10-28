const chai = require("chai");
const expect = chai.expect;
const calculateNumber = require("./2-calcul_chai")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    expect(calculateNumber('SUM',1,2)).to.equal(3)
    expect(calculateNumber('SUM',1,2.5)).to.equal(4)
    expect(calculateNumber('SUM',1,2.2)).to.equal(3)
    expect(calculateNumber('SUM',1,0.2)).to.equal(1)
    expect(calculateNumber('SUM',1,0.5)).to.equal(2)
  })

  it("checks 0s", function() {
    expect(calculateNumber('SUM',0,0.2)).to.equal(0)
    expect(calculateNumber('SUM',0,0.5)).to.equal(1)
  })

  it("checks negs", function() {
    expect(calculateNumber('SUM',1,-0.2)).to.equal(1)
    expect(calculateNumber('SUM',1,-0.5)).to.equal(1)
  })
})
describe("simple 'SUBTRACT' rounded test", function() {
  it("checks equality", function() {
    expect(calculateNumber('SUBTRACT',1,2)).to.equal(-1)
    expect(calculateNumber('SUBTRACT',1,2.5)).to.equal(-2)
    expect(calculateNumber('SUBTRACT',1,2.2)).to.equal(-1)
    expect(calculateNumber('SUBTRACT',1,0.2)).to.equal(1)
    expect(calculateNumber('SUBTRACT',1,0.5)).to.equal(0)
  })

  it("checks 0s", function() {
    expect(calculateNumber('SUBTRACT',0,0.2)).to.equal(0)
    expect(calculateNumber('SUBTRACT',0,0.5)).to.equal(-1)
  })

  it("checks negs", function() {
    expect(calculateNumber('SUBTRACT',1,-0.2)).to.equal(1)
    expect(calculateNumber('SUBTRACT',1,-0.5)).to.equal(1)
  })
})
describe("simple 'DIVIDE' rounded test", function() {
  it("checks equality", function() {
    expect(calculateNumber('DIVIDE',1,2)).to.equal(0.5)
    expect(calculateNumber('DIVIDE',1,4)).to.equal(0.25)
    expect(calculateNumber('DIVIDE',1,2.2)).to.equal(0.5)
    expect(calculateNumber('DIVIDE',1,0.2)).to.equal('Error')
    expect(calculateNumber('DIVIDE',1,0.5)).to.equal(1)
  })

  it("checks 0s", function() {
    expect(calculateNumber('DIVIDE',0,0.2)).to.equal('Error')
    expect(calculateNumber('DIVIDE',0,0.5)).to.equal(0)
  })

  it("checks negs", function() {
    expect(calculateNumber('DIVIDE',-1,0)).to.equal('Error')
    expect(calculateNumber('DIVIDE',1,-0.5)).to.equal('Error')
  })
})
