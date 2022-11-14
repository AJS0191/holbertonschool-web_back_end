const express = require('express')
const app = express()
const port = 1245

var server = app.listen(port, () => {
  console.log("I'm listening...")})

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts))
})

app.get('/list_products/:itemId([0-9]+)', (req, res) => {
  var item = getItemById(req.params.itemId);
  console.log(req.params.itemId)
  if (item == null){
    res.send(JSON.stringify({"status":"Product not found"}))
  }
  var stock = client.hget(item.id, 'stock');
  var reserved = client.hget(item.id, 'reservedStock')
  if (stock - reserved == 0) {
    res.send(JSON.stringify({"status":"Not enough stock available","itemId":`${item.id}`}))
  }
  client.hset(item.id, 'reservedStock', reserved + 1)
  res.send(JSON.stringify({"status":"Reservation confirmed","itemId":`${item.id}`}))
})

import { createClient } from 'redis';
import { print } from 'redis'
const client = createClient();

const listProducts = [
  {
    'id': 1,
    'name': 'Suitcase 250',
    'price': 50,
    'stock': 4,
  },
  {
    'id': 2,
    'name': 'Suitcase 450',
    'price': 100,
    'stock': 10,
  },
  {
    'id': 3,
    'name': 'Suitcase 650',
    'price': 350,
    'stock': 2,
  },
  {
    'id': 4,
    'name': 'Suitcase 1050',
    'price': 550,
    'stock': 5,
  }
]

listProducts.forEach((item) => {
  client.hset(item.id, 'id', item.id, print)
  client.hset(item.id, 'name', item.name, print)
  client.hset(item.id, 'price', item.price, print)
  client.hset(item.id, 'stock', item.stock, print)
  client.hset(item.id, 'reservedStock', 0, print)
})

function reserveStockById(itemId, stock) {
  client.hset(itemId, 'reservedStock', stock, print);
}

async function getCurrentReservedStockById(itemId) {
  return client.hget(itemId, 'reservedStock')
}



function getItemById(id) {
  listProducts.forEach(item => {
    if (item.id == id) {return item}
    else {return null}

  }); 
}

