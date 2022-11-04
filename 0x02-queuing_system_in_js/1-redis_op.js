import { createClient } from 'redis';
import { print } from 'redis'

const client = createClient();

client.on('error', (err) => { console.log("Redis client not connected to server: " + err)});
client.on('connect', () => { console.log("Redis client connected to the server")});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, print);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransisco', '100');
displaySchoolValue('HolbertonSanFransisco');
