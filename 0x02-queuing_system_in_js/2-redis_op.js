import { createClient } from 'redis';
import { print } from 'redis'

const client = createClient();

client.on('error', (err) => { console.log("Redis client not connected to server: " + err)});
client.on('connect', () => { console.log("Redis client connected to the server")});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  return new Promise((resolve, reject) => {
    if (reject) {
      console.log(reject)
    }
    if (resolve) {
      client.get(schoolName, (err, reply) => {
      console.log(reply);
    })}
})};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransisco', '100');
displaySchoolValue('HolbertonSanFransisco');
