request = require('request')
const chai = require('chai')
const expect = chai.expect

describe('api tests', function() {
  it('testing get method', () => new Promise((done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200)
      expect(response.request.method).to.equal('GET')
      done();
    })
  })
)})
