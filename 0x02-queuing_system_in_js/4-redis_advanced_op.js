import { createClient } from 'redis';
import { print } from 'redis'

const client = createClient();

client.on('error', (err) => { console.log("Redis client not connected to server: " + err)});
client.on('connect', () => { console.log("Redis client connected to the server")});

const schoolList = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
};

client.hset('HolbertonSchools', schoolList, print);
client.hgetall('HolbertonSchools');
