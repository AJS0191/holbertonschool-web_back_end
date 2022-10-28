const assert = require("assert")
const calculateNumber = require("./0-calcul")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2), 3)
    assert.equal(calculateNumber(1,2.5), 4)
    assert.equal(calculateNumber(1,2.2), 3)
    assert.equal(calculateNumber(1,0.2), 1)
    assert.equal(calculateNumber(1,0.5), 2)
  })
})
