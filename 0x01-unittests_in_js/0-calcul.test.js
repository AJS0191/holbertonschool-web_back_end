const assert = require("assert")
const calculateNumber = require("./0-calcul")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2), 3)
  })
})
