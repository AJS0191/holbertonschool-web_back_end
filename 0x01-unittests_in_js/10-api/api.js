const express = require('express')

app = express()

var server = app.listen(7865, function () {
  console.log("API available on localhost port 7865")
})

app.get('/', function(req, res){
  res.send('Welcome to the payment system')
})

app.get('/cart/:id([0-9])+', function(req, res){
  res.send(`Payment methods for cart ${req.params.id}`)
})

app.get('/available_payments', function(req, res){
  payments = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  }
  res.json(payments)
})
.post('/login', function(req, res){
  res.send(`Welcome ${req.body.userName}`)
})
