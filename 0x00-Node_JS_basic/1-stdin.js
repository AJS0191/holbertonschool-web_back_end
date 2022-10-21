// takes info from user and displays
const readline = require('readline');
function nameIs() {
  const rl = readline.createInterface(
    process.stdin, process.stdout,
  );

  rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
    console.log(`Your name is: ${name}`);
    console.log('This important software is now closing');
    rl.close();
  });
}
nameIs();
