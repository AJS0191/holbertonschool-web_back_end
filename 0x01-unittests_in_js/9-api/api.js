const express = require('express')

app = express()

var server = app.listen(7865, function () {
  console.log("API available on localhost port 7865")
})

app.get('/', function(req, res){
  res.send('Welcome to the payment system')
})

app.get('/cart/:id([0-9])+', function(req, res){
  res.send('Welcome to the payment system')
})
