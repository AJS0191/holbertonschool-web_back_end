const assert = require("assert")
const calculateNumber = require("./1-calcul")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2, 'SUM'), 3)
    assert.equal(calculateNumber(1,2.5, 'SUM'), 4)
    assert.equal(calculateNumber(1,2.2, 'SUM'), 3)
    assert.equal(calculateNumber(1,0.2, 'SUM'), 1)
    assert.equal(calculateNumber(1,0.5, 'SUM'), 2)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber(0,0.2, 'SUM'), 0)
    assert.equal(calculateNumber(0,0.5, 'SUM'), 1)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber(1,-0.2, 'SUM'), 1)
    assert.equal(calculateNumber(1,-0.5, 'SUM'), 0)
  })
})
describe("simple 'SUBTRACT' rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2, 'SUBTRACT'), 1)
    assert.equal(calculateNumber(1,2.5, 'SUBTRACT'), 2)
    assert.equal(calculateNumber(1,2.2, 'SUBTRACT'), 1)
    assert.equal(calculateNumber(1,0.2, 'SUBTRACT'), -1)
    assert.equal(calculateNumber(1,0.5, 'SUBTRACT'), 0)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber(0,0.2, 'SUBTRACT'), 0)
    assert.equal(calculateNumber(0,0.5, 'SUBTRACT'), 1)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber(1,-0.2, 'SUBTRACT'), -1)
    assert.equal(calculateNumber(1,-0.5, 'SUBTRACT'), -2)
  })
})
describe("simple 'DIVIDE' rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2, 'DIVIDE'), 0.5)
    assert.equal(calculateNumber(1,2.5, 'DIVIDE'), 0.33)
    assert.equal(calculateNumber(1,2.2, 'DIVIDE'), 0.5)
    assert.equal(calculateNumber(1,0.2, 'DIVIDE'), 'Error')
    assert.equal(calculateNumber(1,0.5, 'DIVIDE'), 1)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber(0,0.2, 'DIVIDE'), 'Error')
    assert.equal(calculateNumber(0,0.5, 'DIVIDE'), 0)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber(1,-0.2, 'DIVIDE'), 'Error')
    assert.equal(calculateNumber(1,-0.5, 'DIVIDE'), -1)
  })
})
