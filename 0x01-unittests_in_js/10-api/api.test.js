request = require('request')
const chai = require('chai')
const expect = chai.expect

describe('api tests', function() {
  it('testing get method', () => new Promise((done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200)
      expect(response.request.method).to.equal('GET')
      expect(body).to.equal('Welcome to the payment system')
      done();
    })
  }))

  it('testing get method with correct cart id', () => new Promise((done) => {
    request('http://localhost:7865/cart/2', (error, response, body) => {
      expect(response.statusCode).to.equal(200)
      expect(body).to.equal('Payment methods for cart 2')
        done();
    })
  }))

  it('testing get method with correct cart id', () => new Promise((done) => {
    request('http://localhost:7865/cart/coco', (error, response, body) => {
      expect(response.statusCode).to.equal(404)
        done();
    })
  }))

  it('testing get method', () => new Promise((done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200)
      expect(response.request.method).to.equal('GET')
      expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}')
      done();
    })
  }))
  })
