const assert = require("assert")
const calculateNumber = require("./1-calcul")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber('SUM',1,2), 3)
    assert.equal(calculateNumber('SUM',1,2.5), 4)
    assert.equal(calculateNumber('SUM',1,2.2), 3)
    assert.equal(calculateNumber('SUM',1,0.2), 1)
    assert.equal(calculateNumber('SUM',1,0.5), 2)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber('SUM',0,0.2), 0)
    assert.equal(calculateNumber('SUM',0,0.5), 1)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber('SUM',1,-0.2), 1)
    assert.equal(calculateNumber('SUM',1,-0.5), 1)
  })
})
describe("simple 'SUBTRACT' rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber('SUBTRACT',1,2), -1)
    assert.equal(calculateNumber('SUBTRACT',1,2.5), -2)
    assert.equal(calculateNumber('SUBTRACT',1,2.2), -1)
    assert.equal(calculateNumber('SUBTRACT',1,0.2), 1)
    assert.equal(calculateNumber('SUBTRACT',1,0.5), 0)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber('SUBTRACT',0,0.2), 0)
    assert.equal(calculateNumber('SUBTRACT',0,0.5), -1)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber('SUBTRACT',1,-0.2), 1)
    assert.equal(calculateNumber('SUBTRACT',1,-0.5), 1)
  })
})
describe("simple 'DIVIDE' rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber('DIVIDE',1,2), 0.5)
    assert.equal(calculateNumber('DIVIDE',1,4), 0.25)
    assert.equal(calculateNumber('DIVIDE',1,2.2), 0.5)
    assert.equal(calculateNumber('DIVIDE',1,0.2), 'Error')
    assert.equal(calculateNumber('DIVIDE',1,0.5), 1)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber('DIVIDE',0,0.2), 'Error')
    assert.equal(calculateNumber('DIVIDE',0,0.5), 0)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber('DIVIDE',-1,0), 'Error')
    assert.equal(calculateNumber('DIVIDE',1,-0.5), 'Error')
  })
})
