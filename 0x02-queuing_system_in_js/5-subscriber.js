import { createClient } from 'redis';
import { print } from 'redis'

const client = createClient();

client.on('error', (err) => { console.log("Redis client not connected to server: " + err)});
client.on('connect', () => { console.log("Redis client connected to the server")});
client.on('message', (chan, msg) => {
  if (msg == 'KILL_SERVER') {
    client.quit();
  }
  console.log(msg);
})

client.subscribe('holberton school channel') 
